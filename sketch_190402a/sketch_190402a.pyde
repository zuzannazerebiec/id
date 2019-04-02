add_library("pdf")
def setup():
    global img
    global nazwa
    global ext
    nazwa = "idphoto"
    ext = ".jpg"
    img = loadImage("k.jpg")
    size(600,600, PDF , "mojPDF2.pdf")
    imageMode(CENTER)

def draw():
    global img
    global nazwa
    global ext
    image(img, width/2, height/2)
    s = loadShape("hat2.svg")
    shape(s, 100, -100, 420, 420)
    
    #save(nazwa+" .edited" +ext)
    exit()
