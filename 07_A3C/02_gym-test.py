# Проверка
# Установка под WIndows https://towardsdatascience.com/how-to-install-openai-gym-in-a-windows-environment-338969e24d30
# Build Tools for Visual Studio https://visualstudio.microsoft.com/downloads/ , Windows SDK, MSVC C++
# Swig по ссылке http://www.swig.org/download.html
# pip install gym
# pip install git+https://github.com/Kojoley/atari-py.git # ToyText
# pip install Box2D # + swing для Atari environments
# pip install box2d box2d-kengz
# pip install gym[atari] # Atari
# pip install gym[accept-rom-license]
# pip install gym[box2d]
# Xming https://sourceforge.net/projects/xming/
# Перед запуском IDE: set DISPLAY=:0


import gym
import random


env = gym.make('Pong-v0', render_mode='human')  # Pong-v0, CarRacing-v0, 'Assault-v0')#'Alien-v0')#'AirRaid-v0')
observation = env.reset()
UP_ACTION = 2
DOWN_ACTION = 3
for _ in range(300):
    env.render()
    # choose random action
    action = random.randint(UP_ACTION, DOWN_ACTION)
    # run one step
    observation, reward, done, info = env.step(action)
    # if the episode is over, reset the environment
    if done:
        env.reset()
env.close()


env = gym.make('CartPole-v0')
# env = gym.make('Pong-v0') #'CarRacing-v0')#'Assault-v0')#'Alien-v0')#'AirRaid-v0')
env.reset()

for _ in range(300):
    env.render()
    UP_ACTION = 2
    DOWN_ACTION = 3
    # action = random.randint(UP_ACTION, DOWN_ACTION)
    env.step(env.action_space.sample())

env.close()
# env = gym.make('Pong-v0') #'CarRacing-v0')#'Assault-v0')#'Alien-v0')#'AirRaid-v0')
env.reset()


env = gym.make('Assault-v0', render_mode='human')  # Pong-v0, CarRacing-v0, Assault-v0, Alien-v0, AirRaid-v0
observation = env.reset()
UP_ACTION = 2
DOWN_ACTION = 3
for _ in range(500):
    env.render()
    # choose  action
    action = env.action_space.sample()
    # run one step
    observation, reward, done, info = env.step(action)
    # if the episode is over, reset the environment
    if done:
        env.reset()
env.close()


env = gym.make('CarRacing-v0')  # Pong-v0, CarRacing-v0, Assault-v0, Alien-v0, AirRaid-v0
observation = env.reset()
UP_ACTION = 2
DOWN_ACTION = 3
for _ in range(500):
    env.render()
    # choose  action
    action = env.action_space.sample()
    # run one step
    observation, reward, done, info = env.step(action)
    # if the episode is over, reset the environment
    if done:
        env.reset()
env.close()
