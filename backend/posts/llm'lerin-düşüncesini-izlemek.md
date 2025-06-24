## Temelde Büyük Dil Modelleri (LLM) Nasıl Çalışır?
Büyük Dil Modelleri(LLM); insanlar tarafından tek tek kodlanmak yerine devasa veri setleri, yani internetteki metinler, kitaplar gibi kaynaklardan alınan bilgilerle eğitiliyor. Bu eğitim süreci, LLM'lerin kelimelerin birbirleriyle ilişkisini ve cümle yapısını öğrenmesini sağlıyor. Bu modeller öğrendikleri verileri parçacıklara(token) ayırır ve bir çıktı üretirken de bu parçacıkları kullanır. Yani bir LLM, yazdığı bir kelimeden sonra hangi kelimenin geleceğini eğitildiği veri setindeki parçacık ihtimallerini hesaba katarak tahmin eder.
<br>
Yaptığı tahminler sonrasında doğru çıktıyı verip vermediğini de geri bildirimler yoluyla öğrenir ve karşılaştıkları problemlere karşı kendi stratejisini geliştirir. Büyük dil modellerinde bu stratejileri kavramak ve anlamlandırmak ise çok zordur.
<br>
>Anthropic : This means that we don't understand how models do most of the things they do.
>Bu, modellerin yaptıkları şeylerin çoğunu nasıl yaptığını anlamadığımız anlamına gelir.
<br>
### LLM'ler Nasıl Düşünür?
Yola bazı sorularla çıkalım:
- LLM'ler bir sürü dil konuşabiliyorlar. Peki hangi dilde düşünüyorlar?
- LLM'ler kelimeleri yazarken sadece bir sonraki kelimeye mi odaklanıyorlar yoksa cümleleri sonuna kadar planlayarak mı yazıyorlar?
- Düşünebilen modeller gerçekten düşündüğü adımları mı bize sunuyor yoksa bazen ürettiği yanlış çıktıya sebep mi uyduruyor?

**Anthropic** bu sorulara firmalarının ürettiği **Claude 3.5 Haiku** modeli üzerinde bir nevi *"AI mikroskopu"* ile çalışarak cevap aramış.
LLM'lerin Çoklu Dil Gizemi
LLM'ler bir sürü dil konuşuyorlar ama her dilde konuşmaları için bir bilgiyi her dilde öğrenmiş olmaları mı gerekiyor? Arka planda hangi dili kullanıyor?
Bunu anlamak için Claude modeline "küçük kelimesinin zıttı" farklı dillerde soruluyor ve inceleniyor. <br>
Bu araştırmada tüm dillerde "küçük" kelimesinin zıttını bulurken aynı temel özelliklerin harekete geçtiğini ve çıktıyı üretirken "büyük" kelimesini sorunun diline çevirdiği fark ediliyor. Bu sonuç ise kavramların evrensel olarak anlamlarını öğrendiğini ve belirli bir dile çevirmeden önce soyut bir alanda düşündüğüne dair bir kanıt sağlıyor. Yani bu araştırmaya göre LLM'ler bir dilde bir şeyi öğrendiğinde bu bilgiyi başka dilde konuşurken uygulayabilir. <br>
## LLM'lerin Cümle Yapısı
LLM'lerin cümle kurarken sadece bir sonraki kelimeyi mi planladığını yoksa bir cümlenin tamamını planlayarak mı yazdığını anlamak için kafiyeli şekilde bir şiir yazması isteniyor ve inceleniyor. <br>
Test edilen durum satırları yazarken kafiyeleri önceden planlayarak mı yoksa her satırın sonuna geldiğinde oraya uygun bir kafiye mi bulduğunu deniyor. İki satırlık ve kafiyeli bir şiir yazdırılıyor: <br>
> He saw a carrot and had to grab it, <br>
> His hunger was like a starving rabbit <br>

Bu kısımda fark etmemiz gereken ilk satırda "Bir havuç gördü ve kapması gerekti" cümlesini yazdıktan sonra anlamsal olarak bunu tamamlamak için ikinci satırda bunun gerekçesini ifade eden bir cümle yazıyor: "Açlığı aç bir tavşan gibiydi." <br>
Bu çıktılar üzerine yapılan deneyler Claude'un önceden planlama yaptığını gösterdi. İkinci satıra başlamadan önce, "grab it" ile kafiyeli olabilecek ve konuyla ilgili potansiyel kelimeleri düşünmeye başladığı bulundu. Ardından bu planları akılda tutarak planlanan kelimeyle bitecek bir satır yazdığı anlaşıldı. <br>
Daha sonrasında "rabbit" kavramını temsil eden kısmı değiştirerek tekrar yazması isteniyor ve yine konuyla bağlantıyı koparmadan, olabilecek mantıklı ve kafiyeli bir kelime bularak ve yeni bir cümle hesaplayarak "habit" kelimesini seçiyor. <br>
En son ise kafiyeli olmayan bir "green" kavramı modele dikte ediliyor. Burada da cümleyi değiştirerek yine ilk cümleyi anlamsal olarak tamamlamak ve gerekçelendirecek şekilde bir cümle yazıyor. <br>
Kısaca Claude kafiye yaparken satır sonuna kadar beklemediğini, aksine kafiyeli kelimeleri ve anlamlı yapıyı önceden planladığını ve bu planları değiştirebiliyor. <br>
## LLM'ler ve Matematik
LLM'ler metinler üzerine eğitilmiş modellerdir, bu yüzden bir hesap makinesi gibi çalışmazlar. Yazının başında bahsedildiği gibi kelime tahmin etme üzerine olan bir algoritma mesela bir toplama işlemini nasıl düşünebilir? <br>
Anthropic'in araştırmasına göre Claude bir toplama işlemi için paralel birden fazla metodu kullanıp bunları eşleştiriyor. Mesela, bir yöntem olarak yaklaşık toplam yapıyor ve son haneyi belirliyor; diğer yöntemlerle ise diğer haneleri belirliyor, vb. Bu şekilde paralel birden fazla yol kullanıp bunları birleştirerek sonuca varıyor. Tabii ki burada olay toplama değil, ama bir LLM'in matematiksel konularda nasıl bir strateji izlediğini, nasıl düşündüğünü anlamak için önemli bir nokta olabilir. <br>
İşin ilginç yanı yaptığı toplama işlemini Claude'a sordukları zaman ise klasik alt alta toplama işlemini anlatıyor. Halbuki araştırmayı yapanlar arka planda böyle çalışmadığını anlamıştı. Büyük ihtimal insanların birbirlerine bu şekilde anlattığını eğitildiği veri setinde biliyor olmasından dolayı böyle anlatıyor. Ama kendisinin bizzat bu yöntemi kullanmıyor olması ilginç. <br>
## LLM'lerin Düşünme Adımları
Bildiğimiz üzere çoğu dil modelinde artık düşünme adımlarını görebiliyoruz ( Deepseek R1, Claude 3.7 Sonnet, QwQ, Gemini 2.5 gibi ) peki gerçekten arka planda olan düşünme adımlarını mı görüyoruz yoksa verdikleri cevapları onaylayacak şekilde bir düşünme aşaması mı üretiyorlar? <br>
Anthropic'in araştırmasına göre Claude bazen varmak istediği çıktıya varabilmek için düşünme adımları uyduruyor. Buradaki en büyük sıkıntı ise bu sahte akıl yürütmelerin normal bir yapay zeka halüsinasyonundan bile daha inandırıcı olması. <br>
Claude'a kolay bir şekilde hesaplayamayacağı bir matematik problemi verildiğinde cevabın doğru veya yanlış olmasına bakmaksızın bir cevap veriyor. Aynı zamanda hesaplamaları yaptığını iddia eden düşünme yollarını da üretiyor. Anthropic'in bu yazı boyunca bahsettiğimiz yorumlanabilirlik yöntemi bu hesaplamaları aslında hiç yapmadığını gösteriyor.
Kaynaklara gitmek ve ayrıntılı olarak okumak isteyenler için: https://www.anthropic.com/research/tracing-thoughts-language-model