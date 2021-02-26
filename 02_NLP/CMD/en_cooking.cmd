@echo off
@echo.
@echo Параметры по умолчанию
.\fasttext_exe\fasttext.exe supervised -input .\fasttext_tutorial\cooking.train -output .\model\res_en_model
@pause

@echo.
@echo 100 эпох
.\fasttext_exe\fasttext.exe supervised -epoch 100 -input .\fasttext_tutorial\cooking.train -output .\model\res_en_model_100
@pause

@echo.
@echo Смотрим результаты
@echo "__label__equipment __label__cast-iron How do I fix a cast iron pot that was heated empty for hours?"
.\fasttext_exe\fasttext.exe predict .\model\res_en_model.bin .\fasttext_tutorial\cooking.valid2 3
@pause

@echo.
@echo Проверка качества 5 эпох
@echo   - precishen - точность, сколько в предсказании правильного
@echo   - recall - полнота, сколько правильных ответов покрывается этой моделью
.\fasttext_exe\fasttext test .\model\res_en_model.bin .\fasttext_tutorial\cooking.valid
@pause

@echo.
@echo Смотрим результаты 100 эпох
@echo "__label__equipment __label__cast-iron How do I fix a cast iron pot that was heated empty for hours?"
.\fasttext_exe\fasttext.exe predict .\model\res_en_model_100.bin .\fasttext_tutorial\cooking.valid2 3
@pause

@echo.
@echo Проверка качества 100 эпох
.\fasttext_exe\fasttext test .\model\res_en_model_100.bin .\fasttext_tutorial\cooking.valid
@pause

@echo.
@echo Введите текст для проверки с выводом до 5ти классов: 5ть эпох
.\fasttext_exe\fasttext predict .\model\res_en_model.bin - 5
@pause

@echo.
@echo Введите текст для проверки с выводом до 5ти классов: 100 эпох
.\fasttext_exe\fasttext predict .\model\res_en_model_100.bin - 5
@pause

