from uuid import UUID
import flet as ft
import uuid
# from pyth.plugins.plaintext.writer import PlaintextWriter
# from pyth.plugins.rtf15.reader import Rtf15Reader
from ebooklib import epub
import PyPDF2
from database.database import UserBook


def load_user_book(name_, format_, text_):
    if UserBook.get_or_none((UserBook.name == name_) & (UserBook.format == format_)):
        print('ОШИБКА УЖЕ ЕСТЬ КНИГА')
        return
    else:
        UserBook.create(
            ref_key=uuid.uuid4(),
            name=name_,
            content=text_,
            bookmark=0,
            format=format_
        )


def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text


def extract_text_from_rtf(rtf_path):
    doc = Rtf15Reader.read(open(rtf_path, 'rb'))
    text = PlaintextWriter.write(doc).getvalue()
    return text


def extract_text_from_fb2(fb2_path):
    book = fb2.read_fb2_file(fb2_path)
    text = ""
    for item in book.get_items_of_type(fb2.ITEM_DOCUMENT):
        text += item.get_content().decode('utf-8')
    return text


def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    text = ""
    for item in book.get_items_of_type(epub.ITEM_DOCUMENT):
        text += item.get_content().decode('utf-8')
    return text


def pick_files_result(e: ft.FilePickerResultEvent):
    format_ = e.files[0].name.split('.')[-1]
    name_ = e.files[0].name.replace(format_, '')
    if format_ in ['fb2', 'epub', 'txt', 'rtf', 'pdf', ]:

        if format_ == 'txt':
            text_ = extract_text_from_txt(e.files[0].path)
            load_user_book(name_, format_, text_)
            e.control.update()
            e.page.update()

        if format_ == 'pdf':
            text_ = extract_text_from_pdf(e.files[0].path)
            load_user_book(name_, format_, text_)
            e.page.update()

        if format_ == 'rtf':
            text_ = extract_text_from_rtf(e.files[0].path)
            load_user_book(name_, format_, text_)
            e.page.update()

        if format_ == 'fb2':
            text_ = extract_text_from_fb2(e.files[0].path)
            load_user_book(name_, format_, text_)
            e.page.update()

        if format_ == 'epub':
            text_ = extract_text_from_epub(e.files[0].path)
            load_user_book(name_, format_, text_)
            e.page.update()
    else:
        print('ОШИБКА')
