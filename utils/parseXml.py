from xml.dom import minidom

for i in range(1,3001):
    if i == 2815:
        continue
    mydoc = minidom.parse('../data/artifacts/xml/armas ('+str(i)+').xml')
    filename = mydoc.getElementsByTagName('filename')[0].firstChild.data
    scale_x = 416/int(mydoc.getElementsByTagName('width')[0].firstChild.data)
    scale_y = 416/int(mydoc.getElementsByTagName('height')[0].firstChild.data)
    xmin = int(mydoc.getElementsByTagName('xmin')[0].firstChild.data)*scale_x
    xmax = int(mydoc.getElementsByTagName('xmax')[0].firstChild.data)*scale_x
    ymin = int(mydoc.getElementsByTagName('ymin')[0].firstChild.data)*scale_y
    ymax = int(mydoc.getElementsByTagName('ymax')[0].firstChild.data)*scale_y
    # w = int(mydoc.getElementsByTagName('width')[0].firstChild.data)
    # h = int(mydoc.getElementsByTagName('height')[0].firstChild.data)
    w = 416
    h = 416



    cx = str((xmin+xmax)/(2*w))
    cy = str((ymin+ymax)/(2*h))
    width = str((xmax-xmin)/w)
    height = str((ymax-ymin)/h)
    line = "0 "+cx +" "+cy+" "+width+" "+height
    if float(cx) >= 1 or float(cy) >= 1 or float(width) >= 1 or float(height) >= 1:
        print(filename)
    f = open('../data/artifacts/labels/'+filename+'.txt','w')
    f.write(line)
    f.close()