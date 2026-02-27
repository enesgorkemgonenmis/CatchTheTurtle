Catch The Turtle -
Python'ın Turtle grafik kütüphanesiyle geliştirilmiş, refleks odaklı bir mini oyundur. Bu proje, olay tabanlı programlama (event-driven programming) ve mantık kurma becerilerini geliştirmek amacıyla tasarlanmıştır.

Nasıl Oynanır?
Dosyayı Çalıştırın: Python dosyasını başlattığınızda karşınıza bir karşılama ekranı gelir.
Oyunu Başlatın: Ekranda herhangi bir yere tıklayarak 30 saniyelik geri sayımı başlatın.
Kaplumbağayı Yakalayın: Ekranda rastgele yerlerde beliren yeşil kaplumbağanın üzerine tıklamaya çalışın.
Skor Kazanın: Her başarılı tıklama size 1 puan kazandırır. Kalan süreniz ve skorunuz ekranın üst kısmında anlık olarak güncellenir.
Oyun Sonu: Süre bittiğinde ekran temizlenir ve final skorunuz büyük bir "GAME OVER" yazısıyla gösterilir.

Bu Projede Neler Öğrendim?
Bu projeyi tamamlamak, bana şu temel kavramları pekiştirme fırsatı sundu:
Olay Tabanlı Programlama: Kaplumbağa için .onclick() ve oyun başlangıcı için .onscreenclick() metodlarının kullanımı.
Asenkron Mantık: UI'ı dondurmadan zamanlayıcı ve hareketi yönetmek için .ontimer() metodunun kullanılması.
Global Durum Yönetimi: Skor ve geri sayım gibi verilerin farklı fonksiyonlar arasında global anahtar kelimesiyle koordine edilmesi.
Turtle UI Yönetimi: Skor, zamanlayıcı ve oyun objesi gibi farklı görevler için birden fazla "turtle" objesinin (instance) eş zamanlı yönetilmesi.

Kullanılan Teknolojiler
Python 3.14
Turtle Graphics Library (Standart Kütüphane)
Random Modülü (Koordinat üretimi için)

Kurulum ve Çalıştırma
Bu depoyu (repository) bilgisayarınıza indirin:
git clone https://github.com/KULLANICI_ADIN/catch-the-turtle.git
Proje klasörüne gidin:
cd catch-the-turtle
Oyunu çalıştırın:
python main.py

// Bu proje, Python'ın grafik yeteneklerini keşfetmek için bir öğrenme süreci olarak geliştirilmiştir. //
