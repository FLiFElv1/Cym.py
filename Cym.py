�
    ��f�  �                   �   � d dl Z d dlZd dlZd dlZdZdZdZdZdZdZ	dZ
e� d	e� d	e� �Ze� d
e� de� �Ze� d
e� de� �Zd� Zd� ZdZd� Zd� Zd� Z e�   �          dS )�    Nz
[38;5;46mz
[38;5;15mz[38;5;265mz[38;5;226mz[38;5;123mz[38;5;160mz
[38;5;81m�>�0�1�2c                  �V   � t          j        d�  �         t          t          �  �         d S )N�clear)�os�system�print�logo� �    �/sdcard/download/Cym.pyr   r      s   � �B�I�g����u�T�{�{�{�{�{r   c                  �4   � t          t          � d��  �         d S )Nu�   ──────────────────────────────────────────────────)r   �Yr   r   r   �linexr      s6   � �E�Q�  o�  o�  o�  p�  p�  p�  p�  pr   u  
[1;34mhttps://t.me/f7lifel
[1;30m------------------------------------------
[1;31m
███████╗███╗   ██╗ ██████╗  ██████╗██╗   ██╗
██╔════╝████╗  ██║██╔════╝ ██╔════╝╚██╗ ██╔╝
█████╗  ██╔██╗ ██║██║█████╗██║      ╚████╔╝ 
██╔══╝  ██║╚██╗██║██║╚════╝██║       ╚██╔╝  
███████╗██║ ╚████║╚██████╗ ╚██████╗   ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝   ╚═╝c                  �  � t          �   �          t          dt          � d��  �         t          t          � d��  �         t	          �   �          t          t          � d��  �        } | dv rt          �   �          | dv rt          �   �          d S t	          �   �          t          t          � d��  �         t	          �   �          t          j
        d�  �         t          t          � d	��  �         t          j
        d�  �         t          �   �          d S )
Nz[1;30mu!    بدء تشفير [1;30mCython u"    بدء تشفير [1;30mMarshal u    اختر : )r   )r   u     الخيار غير موجود �   u    حاول مرة أخرى )r   r   �xd1�xd2r   �input�xd�___cythonx___�___marshalx___�time�sleep�
___swag___)�options    r   r   r      s�   � �	�G�G�G�	�
@�s�
@�
@�
@�A�A�A�	�S�
7�
7�
7�8�8�8�	�G�G�G��b�&�&�&�'�'�F�������������������������5�5�5�6�6�6������
�1������/�/�/�0�0�0��
�1���������r   c                  ��  � t          �   �          t          t          � dt          � dt          � dt          � dt          � d�
�  �         t          �   �          t          t          � d��  �        } t          �   �          t          t          � d��  �         t          �   �          t          j        d| � ��  �         t          �   �          t          t          � d��  �         t          �   �          d S )	Nu    مثال : F.py �|z [1;30mflifel.py z [1;30mFlifel.py �    أدخل اسم ملفك : u$    في انتظار تشفير Cythonzcythonize -b u    تشفير Cython ناجح)
r   r   r   r   �Wr   r   r	   r
   �exit)�encfilexs    r   r   r   #   s�   � �	�G�G�G�	�R�
Z�
Z�!�
Z�
Z�a�
Z�
Z�a�
Z�
Z�!�
Z�
Z�
Z�[�[�[�	�G�G�G���8�8�8�9�9�H�	�G�G�G�	�R�
5�
5�
5�6�6�6�	�G�G�G��I�(�h�(�(�)�)�)�	�G�G�G�	�R�
,�
,�
,�-�-�-��F�F�F�F�Fr   c                  �  � t          �   �          t          t          � dt          � dt          � d��  �         t          �   �          t          t          � d��  �        } 	 | �                    d�  �        }|d         dz   }n#  t          t          � d��  �        }Y nxY wt          t          t          � d	��  �        �  �        }t          �   �          t          | �  �        �
                    �   �         }	 d}t          |�  �        D ]�}|d
z  }t          |dd�  �        }t          j        |�  �        }dt          |�  �        z   dz   }	t!          j        d�  �         t          t          � dt$          � d�t'          |�  �        z   �  �         ��nO# t(          $ r t+          t          � d��  �         Y n,t,          $ r  t+          t          � d�| z   dz   �  �         Y nw xY wt          �   �          t          |d�  �        }
|
�                    |	�  �         |
�                    �   �          t          t          � dt$          � d�|z   �  �         d S )Nu    مثال : /sdcard/f.py r    z /sdcard/f.py r!   �.r   z_enc.pyu%    أدخل اسم حفظ الملف : u'    حد عدد مرات التشفير : r   � �execuP   #تم التشفير بواسطة فليفل

import marshal
exec(marshal.loads(z))g����Mbp?u!    عدد مرات التشفير :u#    قيمة الإدخال خاطئةu    الملف u    غير موجود�wu(    ملفك المشفر محفوظ كـ :)r   r   r   r   r"   r   r   �split�int�open�read�range�compile�marshal�dumps�reprr   r   �G�str�
ValueErrorr#   �FileNotFoundError�write�close)�x�q�u�f�a�j�i�m�k�t�ls              r   r   r   0   sK  � �	�G�G�G�	�R�
?�
?�!�
?�
?�a�
?�
?�
?�@�@�@�	�G�G�G���1�1�1�2�2�A�@��G�G�C�L�L���a�D�9�����@��R�>�>�>�?�?��������E�R�@�@�@�A�A�B�B�A�	�G�G�G��Q�������A�=����q��� 	I� 	I�A���F�A���3��'�'�A���a� � �A�e�fj�kl�fm�fm�m�nr�r�A��J�u�����R�>�>�!�>�>�>��Q���G�H�H�H�H�	I�� � 9� 9� 9���7�7�7�8�8�8�8�8�� =� =� =��� � � �1�$�';�;�<�<�<�<�<�=����	�G�G�G��Q����A��G�G�A�J�J�J��G�G�I�I�I�	�R�
=�
=��
=�
=�
=��
A�B�B�B�B�Bs%   � A= �=B�/BF �!G�)&G�G)�cythonr	   r   r0   r3   r"   �Br   �A�R�Or   r   r   r   r   r   r   r   r   r   r   r   �<module>rI      s�   �� � � � � � � � � � � � � � � � ���O�!�&6�A�9I�q�L\�!�_o�]^�  sB�pq��>�>�!�>�>�a�>�>���n�n�Q�n�n��n�n�#�A������A���S� *� *� *� p�  p�  p�	o��� � �&� � �C� C� C�@ �
�����r   