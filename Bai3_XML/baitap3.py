from xml.dom.minidom import Document
import xml.dom.minidom
import os.path

def make_xml(path_file,cd):
    if (os.path.isfile(path_file)):
        doc = xml.dom.minidom.parse(path_file)
        root_xml = doc.documentElement

    else:
        doc = Document()
        root_xml = doc.createElement('cds')
        doc.appendChild(root_xml)

    child_node = doc.createElement('cd')
    child_node.setAttribute('ten', cd.ten)
    root_xml.appendChild(child_node)

    ca_sy = doc.createElement('ca_sy')
    ca_sy.appendChild(doc.createTextNode(cd.ca_sy))
    child_node.appendChild(ca_sy)

    so_bai_hat = doc.createElement('so_bai_hat')
    so_bai_hat.appendChild(doc.createTextNode(cd.so_bai_hat))
    child_node.appendChild(so_bai_hat)

    gia_thanh = doc.createElement('gia_thanh')
    gia_thanh.appendChild(doc.createTextNode(cd.gia_thanh))
    child_node.appendChild(gia_thanh)

    return doc

def read_xml(path_file):
    DOMTree = xml.dom.minidom.parse(path_file)
    collection = DOMTree.documentElement

    cds = collection.getElementsByTagName('cd')

    for cd in cds:
        print('----- CD -----')
        if cd.hasAttribute('ten'):
            print('Tên CD: %s' % cd.getAttribute('ten'))
        ca_sy = cd.getElementsByTagName('ca_sy')[0]
        print ('Ca sỹ: %s' % ca_sy.childNodes[0].data)
        so_bai_hat = cd.getElementsByTagName('so_bai_hat')[0]
        print ('Format: %s' % so_bai_hat.childNodes[0].data)
        gia_thanh = cd.getElementsByTagName('gia_thanh')[0]
        print ('Rating: %s' % gia_thanh.childNodes[0].data)

class cd():
    def __init__(self,ten,ca_sy,so_bai_hat,gia_thanh):
        self.ten = ten
        self.ca_sy = ca_sy
        self.so_bai_hat = so_bai_hat
        self.gia_thanh = gia_thanh


if __name__ == "__main__":
    tt = 1
    while tt == 1:
        todo = int(input('Bạn muốn làm gì? 1: Thêm mới, 2: Xem danh sách CD\t'))
        if todo == 1:
            ten = input('Nhập tên CD: \t')
            ca_sy = input('Nhập tên ca sỹ: \t')
            so_bai_hat = input('Nhập số bài hát: \t')
            gia_thanh = input('Giá thành: \t')
            cd = cd(ten,ca_sy,so_bai_hat,gia_thanh)
            make_xml('files_xml/cd.xml',cd).writexml(open(file='files_xml/cd.xml',mode = 'w',encoding='utf8'),indent='',addindent='',newl='')
            print('Đã thêm CD')
        elif todo == 2:
            read_xml('files_xml/cd.xml')
        tt = int(input('Bạn có muốn tiếp tục không? (1: có, 2: không) '))