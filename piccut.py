import os
# python3 -m pip install pillow
try:
    from PIL import Image
except ImportError:
    os.system("python -m pip install pillow")
    from PIL import Image

def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]
        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext))
                num = num + 1
    else:
        print('长宽不满足切割要求!')

if __name__ == '__main__':
    src = input('图片文件：')
    if os.path.isfile(src):
        dstpath = input('图片输出目录：')
        if (dstpath == '') or os.path.exists(dstpath):
            row = int(input('行数：'))
            col = int(input('列数：'))
            if row > 0 and col > 0:
                splitimage(src, row, col, dstpath)
            else:
                print('无效')
        else:
            print('输出不存在！' % dstpath)
    else:
        print('图片不存在！{}'.format(src))
