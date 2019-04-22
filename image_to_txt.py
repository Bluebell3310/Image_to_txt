from PIL import Image

def image_to_txt(imgName, maxSize):
    # 打開圖片
    print("開啟圖片[{}]".format(imgName))
    try:
        img = Image.open(imgName)
    except:
        print("開啟圖片[{}]時出現錯誤".format(imgName))
    
    # 顯示圖片資訊
    print("圖片資訊: 大小為{}x{}, 格式為{}, 色彩模式為{}".format(img.size[0], img.size[1], img.format, img.mode))
    
    # 確認色彩模式是否為RGB，如果不是則轉換
    if img.mode != 'RGB':
        print("圖片顏色編碼不是RGB，進行轉換")    
        img = img.convert('RGB')
        print("轉換完成")

    width = img.size[0]
    height = img.size[1]

    # 如果圖片寬大於指定數值，則進行圖片縮小
    zoom = 0 # 縮小比率
    if width >= maxSize:
        zoom = width / maxSize
        width = int(width / zoom) 
        height = int(height / zoom) 
        height = int(height / 2) # 除2讓比例看起來比較正確
        img = img.resize((width, height))
        print("圖片寬於{}，已縮小為{}x{}".format(maxSize, img.size[0], img.size[1]))
    
    # 把圖片轉換為純黑白
    img = img.convert('1')

    # 開始轉換程序
    namestr = imgName.split('.')[0] + '.txt'
    txt = open(namestr, 'w')
    print()
    print('開始進行圖片轉txt程序')
    print('...')
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # print('x= ', x, 'y= ', y, 'pixel= ', pixel)
            if pixel != 0:
                txt.write(' ')
            else:
                txt.write('@')
        txt.write('\n')
    
    print('程序執行完成')
    print('檔案儲存為[{}]'.format(namestr))
    txt.close()
    print('保存完成')

name = input('請輸入圖片檔案名稱(圖片需置於同一層資料夾): ')
maxSize = int(input('請輸入最大寬度(100~500): '))
if maxSize < 100 or maxSize > 500:
    print('輸入錯誤')
else:
    image_to_txt(name, maxSize)
print('程式結束')