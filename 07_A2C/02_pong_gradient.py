# Источник http://karpathy.github.io/2016/05/31/rl/

# Как установить gym под windows
# https://towardsdatascience.com/how-to-install-openai-gym-in-a-windows-environment-338969e24d30
""" Trains an agent with (stochastic) Policy Gradients on Pong. Uses OpenAI Gym. """

import numpy as np
import pickle
import gym
import os

resume = True  # resume from previous checkpoint if file exist?
render = True

# Hyperparameters
hidden_neurons = 200  # number of hidden layer neurons
batch_size = 10  # every how many episodes to do a param update?
learning_rate = 1e-4
gamma = 0.99  # discount factor for reward
decay_rate = 0.99  # decay factor for RMSProp leaky sum of grad^2

ACTION_UP = 2
ACTION_DOWN = 3

# Model initialization
dimension = 80 * 80  # input dimensionality: 80x80 grid
MODEL_FILE_NAME = 'models/save.pcl'


def init_model():
    if resume and os.path.exists(MODEL_FILE_NAME):
        model = pickle.load(open(MODEL_FILE_NAME, 'rb'))
        print('Loaded model from', MODEL_FILE_NAME)
    else:
        model = {}
        model['W1'] = np.random.randn(hidden_neurons, dimension) / np.sqrt(dimension)  # "Xavier" initialization
        model['W2'] = np.random.randn(hidden_neurons) / np.sqrt(hidden_neurons)
    return model


def sigmoid(x):
    """sigmoid "squashing" function to interval [0,1]"""
    return 1.0 / (1.0 + np.exp(-x))


def preparation_image(image):
    """ prepro 210x160x3 uint8 frame into 6400 (80x80) 1D float vector """
    image = image[35:195]  # crop 210x160 => 160x160
    image = image[::2, ::2, 0]  # downsample by factor of 2: 160x160 => 80x80
    image[image == 144] = 0  # erase background (background type 1)
    image[image == 109] = 0  # erase background (background type 2)
    image[image != 0] = 1  # everything else (paddles, ball) just set to 1
    return image.astype(np.float64).ravel()


def discount_rewards(r):
    """ take 1D float array of rewards and compute discounted reward """
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            running_add = 0  # reset the sum, since this was a game boundary (pong specific!)
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r


def policy_forward(x, model):
    """ return probability of taking action 2 (UP), and hidden state"""
    h = np.dot(model['W1'], x) # compute hidden layer neuron activations
    h[h < 0] = 0  # ReLU nonlinearity: threshold at zero
    logp = np.dot(model['W2'], h)  # compute log probability of going up
    p = sigmoid(logp) # sigmoid function (gives probability of going up)
    return p, h


def policy_backward(eph, epdlogp, model):
    """ backward pass. (eph is array of intermediate hidden states) """
    dW2 = np.dot(eph.T, epdlogp).ravel()
    dh = np.outer(epdlogp, model['W2'])
    dh[eph <= 0] = 0  # backpro prelu
    dW1 = np.dot(dh.T, epx)
    return {'W1': dW1, 'W2': dW2}


if __name__ == '__main__':
    model = init_model()

    grad_buffer = {k: np.zeros_like(v) for k, v in model.items()}  # model.iteritems() # update buffers that add up gradients over a batch
    rmsprop_cache = {k: np.zeros_like(v) for k, v in model.items()}  # model.iteritems() # rmsprop memory

    env = gym.make("Pong-v0")
    observation = env.reset()
    prev_x = None  # used in computing the difference frame
    xs, hs, dlogps, drs = [], [], [], []
    running_reward = None
    reward_sum = 0
    episode_number = 0
    lose_count = 0
    win_count = 0
    games_count = 0

    while True:
        if render:
            env.render()

        # preprocess the observation, set input to network to be difference image
        cur_x = preparation_image(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(dimension)
        prev_x = cur_x

        # forward the policy network and sample an action from the returned probability
        aprob, h = policy_forward(x, model)
        action = ACTION_UP if np.random.uniform() < aprob else ACTION_DOWN  # roll the dice!


        # record various intermediates (needed later for backprop)
        xs.append(x)  # observation
        hs.append(h)  # hidden state
        y = 1 if action == ACTION_UP else 0  # a "fake label"
        dlogps.append(y - aprob)  # grad that encourages the action that was taken to be taken (see http://cs231n.github.io/neural-networks-2/#losses if confused)

        # step the environment and get new measurements
        observation, reward, done, info = env.step(action)
        reward_sum += reward

        drs.append(reward)  # record reward (has to be done after we call step() to get reward for previous action)

        if reward != 0:  # Pong has either +1 or -1 reward exactly when game ends.
            games_count += 1
            if reward == -1:
                lose_count += 1
            else:
                win_count += 1
            # print(f'ep {episode_number}: game finished, reward: {reward} {"" if reward == -1 else " !!!!!!!!"}')

        if done:  # an episode finished
            episode_number += 1

            # stack together all inputs, hidden states, action gradients, and rewards for this episode
            epx = np.vstack(xs)
            eph = np.vstack(hs)
            epdlogp = np.vstack(dlogps)
            epr = np.vstack(drs)

            xs, hs, dlogps, drs = [], [], [], []  # reset array memory

            # compute the discounted reward backwards through time
            discounted_epr = discount_rewards(epr)
            # standardize the rewards to be unit normal (helps control the gradient estimator variance)
            discounted_epr -= np.mean(discounted_epr)
            discounted_epr /= np.std(discounted_epr)

            epdlogp *= discounted_epr  # modulate the gradient with advantage (PG magic happens right here.)

            grad = policy_backward(eph, epdlogp, model)
            for layer in model:
                grad_buffer[layer] += grad[layer]  # accumulate grad over batch

            # perform rmsprop parameter update every batch_size episodes
            if episode_number % batch_size == 0:
                # for k, v in model.iteritems():
                for layer, v in model.items():
                    g = grad_buffer[layer]  # gradient
                    rmsprop_cache[layer] = decay_rate * rmsprop_cache[layer] + (1 - decay_rate) * g ** 2
                    model[layer] += learning_rate * g / (np.sqrt(rmsprop_cache[layer]) + 1e-5)
                    grad_buffer[layer] = np.zeros_like(v)  # reset batch gradient buffer

            # boring book-keeping
            running_reward = reward_sum if running_reward is None else running_reward * 0.99 + reward_sum * 0.01
            print(f'ep {episode_number}: {games_count} games finished, lose {lose_count}, with reward: {win_count}')
            print(f'    resetting env. episode reward total was {reward_sum}. running mean: {running_reward}')
            if episode_number % 100 == 0:
                pickle.dump(model, open(MODEL_FILE_NAME, 'wb'))
            reward_sum = 0
            observation = env.reset()  # reset env
            prev_x = None
            lose_count = 0
            win_count = 0
            games_count = 0




