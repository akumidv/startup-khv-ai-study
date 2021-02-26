@echo off
@echo.
@echo Параметры по умолчанию
.\fasttext_exe\fasttext.exe supervised -input .\fasttext_tutorial\russian_text.txt -output .\model\res_ru_model
@pause

@echo.
@echo 100 эпох
.\fasttext_exe\fasttext.exe supervised -epoch 100 -input .\fasttext_tutorial\russian_text.txt -output .\model\res_ru_model_100
@pause

@echo.
@echo 1000 эпох
.\fasttext_exe\fasttext.exe supervised -epoch 1000 -input .\fasttext_tutorial\russian_text.txt -output .\model\res_ru_model_1000
@pause


@echo.
@echo Проверка качества 5 эпох
@echo   - precishen - точность, сколько в предсказании правильного
@echo   - recall - полнота, сколько правильных ответов покрывается этой моделью
.\fasttext_exe\fasttext test .\model\res_ru_model.bin .\fasttext_tutorial\russian_test_text.txt
@pause


@echo.
@echo Проверка качества 100 эпох
@echo   - precishen - точность, сколько в предсказании правильного
@echo   - recall - полнота, сколько правильных ответов покрывается этой моделью
.\fasttext_exe\fasttext test .\model\res_ru_model_100.bin .\fasttext_tutorial\russian_test_text.txt
@pause


@echo.
@echo Введите текст для проверки с выводом до 5ти классов: 5ть эпох
.\fasttext_exe\fasttext predict .\model\res_ru_model.bin - 5
@pause

@echo.
@echo Введите текст для проверки с выводом до 5ти классов: 100 эпох
.\fasttext_exe\fasttext predict .\model\res_ru_model_100.bin - 5
@pause

@echo.
@echo Введите текст для проверки с выводом до 5ти классов: 1000 эпох
.\fasttext_exe\fasttext predict .\model\res_ru_model_1000.bin - 5
@pause
