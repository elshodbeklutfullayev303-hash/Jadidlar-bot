# -*- coding: utf-8 -*-
"""
Jadidlar ma'lumotlar bazasi: hayoti, ijodi, tug'ilgan sanasi, joyi, suratlari va hikmatlari.
"""

JADIDLAR = {
    "behbudiy": {
        "name": "Mahmudxo'ja Behbudiy",
        "title": "Jadidchilik harakati asoschisi, ma'rifatparvar alloma",
        "birth_date": "1875-yil 19-yanvar",
        "birth_place": "Samarqand yaqinidagi Baxshitepa qishlog'i",
        "death_date": "1919-yil 25-mart (Qarshi shahrida qatl etilgan)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Mahmudkhoja_Behbudiy.jpg/440px-Mahmudkhoja_Behbudiy.jpg",
        "bio": (
            "Mahmudxo'ja Behbudiy (1875–1919) — Turkiston jadidchilik harakatining yetakchisi, "
            "ulug' ma'rifatparvar, dramaturg, noshir va jamoat arbobi.\n\n"
            "U Samarqandda yangi usul (usuli jadid) maktablarini ochgan, darsliklar yozgan. "
            "1911-yilda yozilgan 'Padarkush' dramasi bilan o'zbek dramaturgiyasiga asos solgan. "
            "Shuningdek, 'Samarqand' gazetasi va 'Oyna' jurnalini tashkil etgan.\n\n"
            "Behbudiy xalqni jaholatdan qutqarishning birdan-bir yo'li ilm-ma'rifat va milliy o'zlikni anglash "
            "deb bilgan. U ikki emas, to'rt tilni (turkiy, forsiy, arabiy, rusiy) bilish zarurligini uqtirgan."
        ),
        "works": [
            "Padarkush yoxud o'qimagan bolaning holi (drama, 1911)",
            "Risolai asbobi savod (Savod chiqarish kitobi)",
            "Risolai jug'rofiyai umroniy (Aholi geografiyasi)",
            "Risolai jug'rofiyai Rusiy (Rossiya geografiyasi)",
            "Kitobat ul-atfol (Bolalar xati)"
        ],
        "quote": "«Dunyoda turmoq uchun dunyoviy fan va ilm lozimdur, zamona ilmidan bebahra millat boshqalarga poymol bo'lur!»",
    },
    "qodiriy": {
        "name": "Abdulla Qodiriy (Julqunboy)",
        "title": "O'zbek romanchiligi asoschisi, buyuk adib",
        "birth_date": "1894-yil 10-aprel",
        "birth_place": "Toshkent shahri",
        "death_date": "1938-yil 4-oktabr (Qatag'on qurboni, Toshkent)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Abdulla_Qodiriy.jpg/440px-Abdulla_Qodiriy.jpg",
        "bio": (
            "Abdulla Qodiriy (1894–1938) — o'zbek adabiyotida professional romanchilik maktabiga asos solgan "
            "buyuk yozuvchi, shoir va tarjimon.\n\n"
            "U o'zining shoh asari bo'lmish 'O'tkan kunlar' (1922) romani bilan o'zbek adabiyotida yangi davrni boshlab berdi. "
            "Keyinroq 'Mehrobdan chayon' tarixiy romanini va 'Obid ketmon' qissasini yozdi. "
            "'Mushtum' jurnali asoschilaridan biri bo'lib, Julqunboy taxallusi bilan satirik asarlar yaratgan.\n\n"
            "1937-yilda sovet qatag'oni qurboni bo'lib hibsga olingan va 1938-yil 4-oktabrda otib tashlangan."
        ),
        "works": [
            "O'tkan kunlar (birinchi o'zbek romani, 1922–1926)",
            "Mehrobdan chayon (tarixiy roman, 1928)",
            "Obid ketmon (qissa, 1934)",
            "Baxtsiz kuyov (drama, 1915)",
            "Kalvak Mahzumning xotira daftaridan, Toshpo'lat tajang nima deydi? (hajviyalar)"
        ],
        "quote": "«Modomiki, biz yangi davrga oyoq qo'ydik, bas, biz har bir yo'sunda ham shu yangi davrning yangiliklari ketidan ergashamiz va shunga o'xshash dostonchiliq, ro'monchiliq va hikoyachiliklarda ham yangarishg'a, xalqimizni shu zamonning 'Tohir-Zuhra'lari, 'Chor darvesh'lari, 'Farhod-Shirin' va 'Bahromgo'r'lari bilan tanishdirishg'a o'zimizda majburiyat his etamiz.»",
    },
    "cholpon": {
        "name": "Abdulhamid Sulaymon o'g'li Cho'lpon",
        "title": "Otashin shoir, tarjimon, milliy uyg'onish jarchisi",
        "birth_date": "1897-yil",
        "birth_place": "Andijon shahri, Qatag'on mahallasi",
        "death_date": "1938-yil 4-oktabr (Qatag'on qurboni, Toshkent)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Abdulhamid_Cho%27lpon.jpg/440px-Abdulhamid_Cho%27lpon.jpg",
        "bio": (
            "Abdulhamid Cho'lpon (1897–1938) — yangi o'zbek she'riyatining asoschilaridan biri, otashin vatanparvar shoir, "
            "nosir, dramaturg va tarjimon.\n\n"
            "Cho'lpon millat erki va ozodligi kuychisi bo'lgan. Uning 'Kecha va kunduz' romani o'zbek nasrining "
            "noyob durdonasidir. U Shekspirning 'Hamlet' fojiasini, Pushkinning 'Boris Godunov' asarini o'zbek tiliga yuksak mahorat bilan tarjima qilgan.\n\n"
            "Shoir 1937-yilda qamoqqa olinib, 1938-yil 4-oktabrda qatag'on qurboni bo'lgan."
        ),
        "works": [
            "Kecha va kunduz (roman, 1936)",
            "Uyg'onish (she'riy to'plam, 1922)",
            "Buloqlar (she'riy to'plam, 1924)",
            "Tong sirlari (she'riy to'plam, 1926)",
            "Yorqinoy (pesa, 1920)"
        ],
        "quote": "«Ko'ngil, sen bunchalar nega / Kishanlar birla do'stlashding? / Na faryoding, na doding bor, / Nechun sen muncha sustlashding?!»",
    },
    "fitrat": {
        "name": "Abdurauf Fitrat",
        "title": "Faylasuf, tilshunos olim, jadid adabiyoti yo'lboshchisi",
        "birth_date": "1886-yil",
        "birth_place": "Buxoro shahri",
        "death_date": "1938-yil 4-oktabr (Qatag'on qurboni, Toshkent)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Abdurauf_Fitrat.jpg/440px-Abdurauf_Fitrat.jpg",
        "bio": (
            "Abdurauf Fitrat (1886–1938) — buyuk alloma, faylasuf, yozuvchi, dramaturg va o'zbek tilshunosligining tamal toshini qo'ygan olim.\n\n"
            "Istanbul dorilfununida ta'lim olgan. Buxoro jadidlarining yetakchisi bo'lgan. "
            "Uning 'Munozara', 'Sayha', 'Hind sayyohi bayonoti' kabi asarlari musulmon dunyosida katta aks-sado bergan. "
            "O'zbekistonda ilk bor professor unvonini olgan olimlardan biri.\n\n"
            "Fitrat ham 1938-yil 4-oktabrda boshqa o'zbek ziyolilari qatori qatag'on qurboni bo'lgan."
        ),
        "works": [
            "Munozara (1909)",
            "Hind sayyohi bayonoti (1912)",
            "O'g'uzxon (drama)",
            "Abulfayzxon (tarixiy tragediya, 1924)",
            "Sarf va Nahv (O'zbek tili grammatikasi)"
        ],
        "quote": "«Haq olinur, berilmas!»",
    },
    "avloniy": {
        "name": "Abdulla Avloniy",
        "title": "Ulug' ma'rifatparvar, murabbiy, jamoat arbobi",
        "birth_date": "1878-yil 12-iyul",
        "birth_place": "Toshkent shahri, Mergancha mahallasi",
        "death_date": "1934-yil 25-avgust (Toshkent)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Abdulla_Avloniy.jpg/440px-Abdulla_Avloniy.jpg",
        "bio": (
            "Abdulla Avloniy (1878–1934) — taniqli o'zbek ma'rifatparvari, pedagog, shoir, noshir va teatr arbobi.\n\n"
            "Toshkentda yangi usul maktablarini tashkil etgan, kambag'al bolalarni o'qitish uchun 'Jamiyati xayriya' tuzgan. "
            "'Turon' teatr truppasini tuzib, o'zbek milliy professional teatriga asos solgan. "
            "'Shuhrat', 'Osiyo' gazetalarini chop ettirgan.\n\n"
            "Uning 'Turkiy Guliston yoxud axloq' asari milliy pedagogika va axloqning oltin qoidasi hisoblanadi."
        ),
        "works": [
            "Turkiy Guliston yoxud axloq (1913)",
            "Birinchi muallim (1912)",
            "Ikkinchi muallim (1912)",
            "Maktab gulistoni (1915)",
            "Advokatlik osonmi? (komediya)"
        ],
        "quote": "«Tarbiya bizlar uchun yo hayot — yo mamot, yo najot — yo halokat, yo saodat — yo falokat masalasidur.»",
    },
    "munavvarqori": {
        "name": "Munavvarqori Abdurashidxonov",
        "title": "Turkiston jadidchilik harakatining ma'naviy otasi",
        "birth_date": "1878-yil",
        "birth_place": "Toshkent shahri, Shayxontohur dahasi",
        "death_date": "1931-yil 23-may (Moskva, Butirka qamoqxonasida qatl etilgan)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Munavvarqori_Abdurashidxonov.jpg/440px-Munavvarqori_Abdurashidxonov.jpg",
        "bio": (
            "Munavvarqori Abdurashidxonov (1878–1931) — Turkistonda milliy ozodlik va ma'rifat harakatining asoschilaridan biri.\n\n"
            "1901-yilda Toshkentda yangi usul maktabini ochgan. 'Xurshid' gazetasiga asos solgan. "
            "Yoshlarni chet ellarga, jumladan Germaniya va Turkiyaga o'qishga yuborish tashabbuskori bo'lgan. "
            "Turkiston Muxtoriyatining faol rahbarlaridan biri bo'lgan.\n\n"
            "U sovet hukumati tomonidan birinchilardan bo'lib hibsga olingan va 1931-yilda Moskvada qatl etilgan."
        ),
        "works": [
            "Adibi avval (1907)",
            "Adib us-soniy (1907)",
            "Usuli hisob (Arifmetika darsligi, 1911)",
            "Tarixi qavmi turk (Turk xalqlari tarixi)",
            "Yer yuzi (Geografiya darsligi)"
        ],
        "quote": "«Bizni jaholat va xurofot zulmatidan faqat va faqat yosh avlodning to'g'ri ta'lim-tarbiyasi qutqara oladi.»",
    },
    "ibrat": {
        "name": "Ishoqxon Junaydullo o'g'li Ibrat",
        "title": "Poliglot olim, sayyoh, ilk bosmaxona asoschisi",
        "birth_date": "1862-yil",
        "birth_place": "Namangan viloyati, To'raqo'rg'on qishlog'i",
        "death_date": "1937-yil aprel (Andijon qamoqxonasida vafot etgan)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Ishoqxon_Ibrat.jpg/440px-Ishoqxon_Ibrat.jpg",
        "bio": (
            "Ishoqxon Ibrat (1862–1937) — ma'rifatparvar olim, shoir, xattot va tilshunos.\n\n"
            "U Sharq va G'arb mamlakatlariga (Makka, Madina, Qohira, Istanbul, Afina, Rim) sayohat qilgan. "
            "Arab, fors, turk, rus, ingliz, urdu tillarini mukammal bilgan. "
            "1908-yilda Orenburgdan litografik bosmaxona mashinasini olib kelib, To'raqo'rg'onda 'Matbaai Is'hoqiya' nomli ilk bosmaxonani ochgan.\n\n"
            "Uning 'Lug'ati sitta al-alsina' (Olti tilli lug'at) kitobi Markaziy Osiyoda tengi yo'q qomusdir."
        ),
        "works": [
            "Lug'ati sitta al-alsina (6 tilli lug'at, 1901)",
            "Jome' ul-xutut (Yozuvlar majmuasi — dunyo alifbolari tarixi, 1912)",
            "Tarixi madaniyat (Madaniyat tarixi)",
            "Tarixi Farg'ona (Farg'ona tarixi)",
            "Devoni Ibrat (She'rlar to'plami)"
        ],
        "quote": "«Ilm o'rganing, til o'rganing, taraqqiy etgan xalqlardan ibrat oling!»",
    },
    "zohiriy": {
        "name": "Ashurali Zohiriy",
        "title": "Tilshunos olim, matbuotchi, ma'rifat fidoyisi",
        "birth_date": "1885-yil",
        "birth_place": "Qo'qon yaqinidagi Oyim qishlog'i",
        "death_date": "1937-yil 4-oktabr (Qatag'on qurboni)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Ashurali_Zohiriy.jpg/440px-Ashurali_Zohiriy.jpg",
        "bio": (
            "Ashurali Zohiriy (1885–1937) — tilshunos, adabiyotshunos, metodist olim va jurnalist.\n\n"
            "Qo'qon jadidchilik harakatining faol namoyandalaridan. 'El bayrog'i', 'Yurt' gazetalari muharriri bo'lgan. "
            "Alisher Navoiy asarlarini o'rganish va nashr ettirishda katta xizmat ko'rsatgan. "
            "Ilk o'zbekcha-ruscha lug'atlarni tuzgan allomalardan biri.\n\n"
            "1937-yilda sho'ro hukumati tomonidan qamoqqa olinib, otib tashlangan."
        ),
        "works": [
            "Imlo qoidalari (1914)",
            "O'zbek tili darsligi",
            "Ruscha-o'zbekcha mukammal lug'at",
            "Navoiy asarlariga sharhlar"
        ],
        "quote": "«Ona tilini asramoq — millat jonini asramoq demakdir!»",
    }
}

QUIZ_QUESTIONS = [
    {
        "question": "«Padarkush» dramasining muallifi kim?",
        "options": ["Mahmudxo'ja Behbudiy", "Abdulla Qodiriy", "Abdulhamid Cho'lpon", "Abdulla Avloniy"],
        "correct": 0,
        "explanation": "«Padarkush» dramasi 1911-yilda Mahmudxo'ja Behbudiy tomonidan yozilgan bo'lib, o'zbek dramaturgiyasining ilk asaridir."
    },
    {
        "question": "O'zbek adabiyotida birinchi roman hisoblangan «O'tkan kunlar» qachon va kim tomonidan yozilgan?",
        "options": ["Cho'lpon (1936)", "Abdulla Qodiriy (1922-1926)", "Abdurauf Fitrat (1915)", "Hamza (1918)"],
        "correct": 1,
        "explanation": "«O'tkan kunlar» 1922–1926-yillarda Abdulla Qodiriy tomonidan yaratilgan."
    },
    {
        "question": "«Tarbiya bizlar uchun yo hayot — yo mamot, yo najot — yo halokat masalasidur» so'zlari kimga tegishli?",
        "options": ["Munavvarqori", "Mahmudxo'ja Behbudiy", "Abdulla Avloniy", "Ishoqxon Ibrat"],
        "correct": 2,
        "explanation": "Ushbu mashhur hikmat Abdulla Avloniyning «Turkiy Guliston yoxud axloq» asaridan olingan."
    },
    {
        "question": "Olti tilli lug'at («Lug'ati sitta al-alsina») muallifi bo'lgan va o'z bosmaxonasini ochgan ma'rifatparvar kim?",
        "options": ["Ishoqxon Ibrat", "Ashurali Zohiriy", "Munavvarqori", "Fitrat"],
        "correct": 0,
        "explanation": "Ishoqxon Ibrat 6 tilli lug'at tuzgan va 1908-yilda To'raqo'rg'onda o'z litografik bosmaxonasini tashkil qilgan."
    },
    {
        "question": "«Haq olinur, berilmas!» shiori qaysi buyuk jadid allomasiga tegishli?",
        "options": ["Abdulhamid Cho'lpon", "Abdurauf Fitrat", "Abdulla Qodiriy", "Munavvarqori"],
        "correct": 1,
        "explanation": "«Haq olinur, berilmas!» shiori Abdurauf Fitrat tomonidan ilgari surilgan."
    }
]
