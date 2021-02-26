@echo off
@echo.
@echo ��ࠬ���� �� 㬮�砭��
.\fasttext_exe\fasttext.exe supervised -input .\fasttext_tutorial\cooking.train -output .\model\res_en_model
@pause

@echo.
@echo 100 ��
.\fasttext_exe\fasttext.exe supervised -epoch 100 -input .\fasttext_tutorial\cooking.train -output .\model\res_en_model_100
@pause

@echo.
@echo ����ਬ १�����
@echo "__label__equipment __label__cast-iron How do I fix a cast iron pot that was heated empty for hours?"
.\fasttext_exe\fasttext.exe predict .\model\res_en_model.bin .\fasttext_tutorial\cooking.valid2 3
@pause

@echo.
@echo �஢�ઠ ����⢠ 5 ��
@echo   - precishen - �筮���, ᪮�쪮 � �।᪠����� �ࠢ��쭮��
@echo   - recall - ������, ᪮�쪮 �ࠢ����� �⢥⮢ ����뢠���� �⮩ �������
.\fasttext_exe\fasttext test .\model\res_en_model.bin .\fasttext_tutorial\cooking.valid
@pause

@echo.
@echo ����ਬ १����� 100 ��
@echo "__label__equipment __label__cast-iron How do I fix a cast iron pot that was heated empty for hours?"
.\fasttext_exe\fasttext.exe predict .\model\res_en_model_100.bin .\fasttext_tutorial\cooking.valid2 3
@pause

@echo.
@echo �஢�ઠ ����⢠ 100 ��
.\fasttext_exe\fasttext test .\model\res_en_model_100.bin .\fasttext_tutorial\cooking.valid
@pause

@echo.
@echo ������ ⥪�� ��� �஢�ન � �뢮��� �� 5� ����ᮢ: 5�� ��
.\fasttext_exe\fasttext predict .\model\res_en_model.bin - 5
@pause

@echo.
@echo ������ ⥪�� ��� �஢�ન � �뢮��� �� 5� ����ᮢ: 100 ��
.\fasttext_exe\fasttext predict .\model\res_en_model_100.bin - 5
@pause

