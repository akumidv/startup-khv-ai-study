@echo off
@echo.
@echo Параметры по умолчанию
.\fasttext_exe\fasttext.exe supervised -input .\rzhd_comments_tone\review_tone.train.txt -output .\model\res_rzhd_model
@pause

@echo.
@echo 100 эпох
.\fasttext_exe\fasttext.exe supervised -epoch 100 -input .\rzhd_comments_tone\review_tone.train.txt -output .\model\res_rzhd_model_100
@pause


@echo.
@echo Проверка качества 5 эпох
@echo   - precishen - точность, сколько в предсказании правильного
@echo   - recall - полнота, сколько правильных ответов покрывается этой моделью
.\fasttext_exe\fasttext test .\model\res_rzhd_model.bin .\rzhd_comments_tone\review_tone.train.txt
@pause


@echo.
@echo Проверка качества 100 эпох
@echo   - precishen - точность, сколько в предсказании правильного
@echo   - recall - полнота, сколько правильных ответов покрывается этой моделью
.\fasttext_exe\fasttext test .\model\res_rzhd_model_100.bin .\rzhd_comments_tone\review_tone.train.txt
@pause


@echo.
@echo Введите текст для проверки с выводом до 5ти классов: 5ть эпох
.\fasttext_exe\fasttext predict .\model\res_rzhd_model.bin - 5
@pause

@echo.
@echo Введите текст для проверки с выводом до 5ти классов: 100 эпох
.\fasttext_exe\fasttext predict .\model\res_rzhd_model_100.bin - 5
@pause
