@echo off
@echo.
@echo ��ࠬ���� �� 㬮�砭��
.\fasttext_exe\fasttext.exe supervised -input .\rzhd_comments_tone\review_tone.train.txt -output .\model\res_rzhd_model_ngram -wordNgrams 2
@pause

@echo.
@echo 100 ��
.\fasttext_exe\fasttext.exe supervised -epoch 100 -input .\rzhd_comments_tone\review_tone.train.txt -output .\model\res_rzhd_model_100_ngram -wordNgrams 2
@pause


@echo.
@echo �஢�ઠ ����⢠ 5 ��
@echo   - precishen - �筮���, ᪮�쪮 � �।᪠����� �ࠢ��쭮��
@echo   - recall - ������, ᪮�쪮 �ࠢ����� �⢥⮢ ����뢠���� �⮩ �������
.\fasttext_exe\fasttext test .\model\res_rzhd_model_ngram.bin .\rzhd_comments_tone\review_tone.train.txt
@pause


@echo.
@echo �஢�ઠ ����⢠ 100 ��
@echo   - precishen - �筮���, ᪮�쪮 � �।᪠����� �ࠢ��쭮��
@echo   - recall - ������, ᪮�쪮 �ࠢ����� �⢥⮢ ����뢠���� �⮩ �������
.\fasttext_exe\fasttext test .\model\res_rzhd_model_100_ngram.bin .\rzhd_comments_tone\review_tone.train.txt
@pause


@echo.
@echo ������ ⥪�� ��� �஢�ન � �뢮��� �� 5� ����ᮢ: 5�� ��
.\fasttext_exe\fasttext predict .\model\res_rzhd_model_ngram.bin - 5
@pause

@echo.
@echo ������ ⥪�� ��� �஢�ન � �뢮��� �� 5� ����ᮢ: 100 ��
.\fasttext_exe\fasttext predict .\model\res_rzhd_model_100_ngram.bin - 5
@pause
