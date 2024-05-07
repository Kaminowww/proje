import turtle #Turtle modülünü içe aktarır, bu da ekranda çizim yapmak için kullanılır.

# OYUN PENCERESİ
pencere = turtle.Screen() #Oyunun oynandığı pencereyi oluşturur.
pencere.setup(width=800, height=600) #Pencerenin genişliğini ve yüksekliğini belirler.
pencere.title("Ömer Alireisoğlu 2461") #Pencere başlığını ayarlar.
pencere.bgcolor("Black") #Pencerenin arka plan rengini siyah olarak ayarlar.
pencere.tracer(0) #Ekran güncellemelerini kapatır, böylece oyun daha hızlı çalışır.

# RAKET 1
raket1 = turtle.Turtle() #1. raketi oluşturur.
raket1.speed(0) #Raketin hareket hızını ayarlar.
raket1.color("White") #Raketin rengini beyaz olarak ayarlar.
raket1.shape("square") #Raketin şeklini kare olarak ayarlar.
raket1.shapesize(stretch_wid= 5, stretch_len=1) #Raketin boyutunu ayarlar.
raket1.penup() #Raketin kalemi kaldırır, böylece çizim yapmadan hareket eder.
raket1.goto(-350,0) #Raketin başlangıç konumunu belirler.

# RAKET 2
raket2 = turtle.Turtle() #2. raketi oluşturur.
raket2.speed(0) #Raketin hareket hızını ayarlar.
raket2.color("White") #Raketin rengini beyaz olarak ayarlar.
raket2.shape("square") #Raketin şeklini kare olarak ayarlar.
raket2.shapesize(stretch_wid= 5, stretch_len=1) #Raketin boyutunu ayarlar.
raket2.penup() #Raketin kalemi kaldırır, böylece çizim yapmadan hareket eder.
raket2.goto(350,0) #Raketin başlangıç konumunu belirler.

# TOP
top = turtle.Turtle() #Top nesnesini oluşturur.
top.speed(0) #Topun hareket hızını ayarlar.
top.color("White") #Topun rengini beyaz olarak ayarlar.
top.shape("square") #Topun şeklini kare olarak ayarlar.
top.penup() #Topun kalemini kaldırır.
top.goto(0,0) #Topun başlangıç konumunu belirler.
top.changex = 0.1 # Topun x eksenindeki hareket hızını belirler.
top.changey = 0.1 #Topun y eksenindeki hareket hızını belirler.

# SKOR 
skor1 = 0 #Oyuncu 1'in skorlarını başlangıçta sıfır olarak ayarlar.
skor2 = 0 #Oyuncu 2'in skorlarını başlangıçta sıfır olarak ayarlar.

# YAZILAR
yazi = turtle.Turtle() #Skoru göstermek için bir turtle nesnesi oluşturur.
yazi.speed(0) #Yazı nesnesinin hareket hızını ayarlar.
yazi.color("White") #Yazının rengini beyaz olarak ayarlar.
yazi.penup() #Yazının kalemini kaldırır.
yazi.hideturtle() #Yazı nesnesini gizler.
yazi.goto(0,260) #Yazıyı belirli bir konuma getirir.
yazi.write("Oyuncu 1: {} Oyuncu 2: {}".format(skor1, skor2), align="center", font=("Courier", 24, "normal")) #Skoru ekrana yazar.

# FONKSİYONLAR
def raket1_yukari(): #1. raketin yukarı hareketini tanımlar.
    y = raket1.ycor()
    y += 20
    raket1.sety(y)

def raket1_asagi(): #1. raketin aşağı hareketini tanımlar.
    y = raket1.ycor()
    y -= 20
    raket1.sety(y)

def raket2_yukari(): #2. raketin yukarı hareketini tanımlar.
    y = raket2.ycor()
    y += 20
    raket2.sety(y)

def raket2_asagi(): #2. raketin aşağı hareketini tanımlar.
    y = raket2.ycor()
    y -= 20
    raket2.sety(y)

# KLAVYE
pencere.listen() #Klavye girişlerini dinler.
pencere.onkeypress(raket1_yukari, "w") #"w" tuşuna basıldığında raket1_yukari fonksiyonunu çağırır.
pencere.onkeypress(raket1_asagi, "s") #"s" tuşuna basıldığında raket1_asagi fonksiyonunu çağırır.
pencere.onkeypress(raket1_yukari, "W") #"W" tuşuna basıldığında raket1_yukari fonksiyonunu çağırır.
pencere.onkeypress(raket1_asagi, "S") #"S" tuşuna basıldığında raket1_asagi fonksiyonunu çağırır.
pencere.onkeypress(raket2_yukari, "Up") #Yukarı ok tuşuna basıldığında raket2_yukari fonksiyonunu çağırır. 
pencere.onkeypress(raket2_asagi, "Down") #Aşağı ok tuşuna basıldığında raket2_asagi fonksiyonunu çağırır.

# OYUN DÖNGÜSÜ
while True: #Oyunun sürekli olarak çalışmasını sağlar.
    try:
        pencere.update() #Ekranı günceller.

        # TOPU HAREKET ETTİRME
        top.setx(top.xcor() + top.changex) #Topun hareketini sağlar ve x koordinatlarını günceller.
        top.sety(top.ycor() + top.changey) #Topun hareketini sağlar ve y koordinatlarını günceller.

        # TOP KENARA DEĞERSE 
        if top.ycor() > 290: #Topun ekranın üst veya alt kenarına çarpıp çarpmadığını kontrol eder ve gerektiğinde yönünü tersine çevirir.
            top.sety(290)
            top.changey *= -1
        if top.ycor() < -290: #Topun ekranın üst veya alt kenarına çarpıp çarpmadığını kontrol eder ve gerektiğinde yönünü tersine çevirir.
            top.sety(-290)
            top.changey *= -1
        if top.xcor() > 390: #Topun sağ veya sol kenara çarptığını kontrol eder ve skoru günceller.
            top.goto(0,0)
            top.changex *= -1
            skor1 += 1
            yazi.clear()
            yazi.write("Oyuncu 1: {} Oyuncu 2: {}".format(skor1, skor2), align="center", font=("Courier", 24, "normal"))
        if top.xcor() < -390: #Topun sağ veya sol kenara çarptığını kontrol eder ve skoru günceller.
            top.goto(0,0)
            top.changex *= -1
            skor2 += 1
            yazi.clear()
            yazi.write("Oyuncu 1: {} Oyuncu 2: {}".format(skor1, skor2), align="center", font=("Courier", 24, "normal"))

        # RAKET VE TOP ETKİLEŞİMİ 
        if (top.xcor() > 330) and (top.ycor() < raket2.ycor() + 50 and top.ycor() > raket2.ycor() - 50): #Raketi ve topun etkileşimini kontrol eder ve gerektiğinde topun yönünü tersine çevirir.
            top.changex *= -1
        if (top.xcor() < -330) and (top.ycor() < raket1.ycor() + 50 and top.ycor() > raket1.ycor() - 50):
            top.changex *= -1
    except:
        break #Programın düzgün bir şekilde bitirir.