@echo off
@echo.
@echo ��ࠬ���� �� 㬮�砭��
.\fasttext_exe\fasttext.exe supervised -input .\fasttext_tutorial\russian_text.txt -output .\model\res_ru_model
@pause

@echo.
@echo 100 ��
.\fasttext_exe\fasttext.exe supervised -epoch 100 -input .\fasttext_tutorial\russian_text.txt -output .\model\res_ru_model_100
@pause

@echo.
@echo 1000 ��
.\fasttext_exe\fasttext.exe supervised -epoch 1000 -input .\fasttext_tutorial\russian_text.txt -output .\model\res_ru_model_1000
@pause


@echo.
@echo �஢�ઠ ����⢠ 5 ��
@echo   - precishen - �筮���, ᪮�쪮 � �।᪠����� �ࠢ��쭮��
@echo   - recall - ������, ᪮�쪮 �ࠢ����� �⢥⮢ ����뢠���� �⮩ �������
.\fasttext_exe\fasttext test .\model\res_ru_model.bin .\fasttext_tutorial\russian_test_text.txt
@pause


@echo.
@echo �஢�ઠ ����⢠ 100 ��
@echo   - precishen - �筮���, ᪮�쪮 � �।᪠����� �ࠢ��쭮��
@echo   - recall - ������, ᪮�쪮 �ࠢ����� �⢥⮢ ����뢠���� �⮩ �������
.\fasttext_exe\fasttext test .\model\res_ru_model_100.bin .\fasttext_tutorial\russian_test_text.txt
@pause


@echo.
@echo ������ ⥪�� ��� �஢�ન � �뢮��� �� 5� ����ᮢ: 5�� ��
.\fasttext_exe\fasttext predict .\model\res_ru_model.bin - 5
@pause

@echo.
@echo ������ ⥪�� ��� �஢�ન � �뢮��� �� 5� ����ᮢ: 100 ��
.\fasttext_exe\fasttext predict .\model\res_ru_model_100.bin - 5
@pause

@echo.
@echo ������ ⥪�� ��� �஢�ન � �뢮��� �� 5� ����ᮢ: 1000 ��
.\fasttext_exe\fasttext predict .\model\res_ru_model_1000.bin - 5
@pause
