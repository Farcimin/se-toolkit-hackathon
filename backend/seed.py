from database import engine, SessionLocal, Base
from models import Prayer


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Prayer).count() > 0:
        db.close()
        return

    prayers = [
        Prayer(
            category="Daily",
            name_en="Modeh Ani",
            name_he="מודה אני",
            text_hebrew="מוֹדֶה אֲנִי לְפָנֶיךָ מֶלֶךְ חַי וְקַיָּם, שֶׁהֶחֱזַרְתָּ בִּי נִשְׁמָתִי בְּחֶמְלָה, רַבָּה אֱמוּנָתֶךָ.",
            transliteration="Модэ ани лэфанэха, мэлэх хай вэкайам, шэhэхэзарта би нишмати бэхэмла, раба эмунатэха.",
            translation_ru="Благодарю я Тебя, Царь живой и вечный, за то что Ты вернул мне душу мою по милости Своей. Велика вера в Тебя.",
            description="The first prayer said upon waking up in the morning. It is a short declaration of gratitude to God for restoring the soul after sleep.",
            audio_url="/audio/modeh_ani.mp3",
            order_index=1,
        ),
        Prayer(
            category="Daily",
            name_en="Shema Yisrael",
            name_he="שְׁמַע יִשְׂרָאֵל",
            text_hebrew="שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד. בָּרוּךְ שֵׁם כְּבוֹד מַלְכוּתוֹ לְעוֹלָם וָעֶד.",
            transliteration="Шма Йисраэль, Адонай Элоhэйну, Адонай Эхад. Барух шэм квод малхуто лэолам ваэд.",
            translation_ru="Слушай, Израиль: Господь — Бог наш, Господь — Един. Благословенно имя славного царства Его во веки веков.",
            description="The most important prayer in Judaism — a declaration of the oneness of God. Recited twice daily, in the morning (Shacharit) and evening (Maariv) services.",
            audio_url="/audio/shema.mp3",
            order_index=2,
        ),
        Prayer(
            category="Daily",
            name_en="Amidah (Shmoneh Esrei) — Opening",
            name_he="עֲמִידָה",
            text_hebrew="אֲדֹנָי שְׂפָתַי תִּפְתָּח וּפִי יַגִּיד תְּהִלָּתֶךָ. בָּרוּךְ אַתָּה יְהוָה, אֱלֹהֵינוּ וֵאלֹהֵי אֲבוֹתֵינוּ, אֱלֹהֵי אַבְרָהָם, אֱלֹהֵי יִצְחָק, וֵאלֹהֵי יַעֲקֹב.",
            transliteration="Адонай сфатай тифтах уфи ягид тэhилатэха. Барух Ата Адонай, Элоhэйну вэЭлоhэй авотэйну, Элоhэй Авраhам, Элоhэй Ицхак, вэЭлоhэй Яаков.",
            translation_ru="Господь, уста мои открой, и рот мой возвестит хвалу Тебе. Благословен Ты, Господь, Бог наш и Бог отцов наших, Бог Авраама, Бог Ицхака и Бог Яакова.",
            description="The central prayer of Jewish liturgy, also called Shmoneh Esrei (Eighteen Blessings). Recited standing, three times daily. This is the opening blessing (Avot).",
            audio_url="/audio/amidah_opening.mp3",
            order_index=3,
        ),
        Prayer(
            category="Blessings",
            name_en="Blessing over Bread (Hamotzi)",
            name_he="הַמּוֹצִיא",
            text_hebrew="בָּרוּךְ אַתָּה יְהוָה אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, הַמּוֹצִיא לֶחֶם מִן הָאָרֶץ.",
            transliteration="Барух Ата Адонай, Элоhэйну Мэлэх hаолам, hамоци лэхэм мин hаарэц.",
            translation_ru="Благословен Ты, Господь, Бог наш, Царь вселенной, выращивающий хлеб из земли.",
            description="A blessing recited before eating bread. It is one of the most commonly used blessings in daily Jewish life.",
            audio_url="/audio/hamotzi.mp3",
            order_index=4,
        ),
        Prayer(
            category="Blessings",
            name_en="Blessing over Wine (Kiddush)",
            name_he="קִדּוּשׁ",
            text_hebrew="בָּרוּךְ אַתָּה יְהוָה אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, בּוֹרֵא פְּרִי הַגָּפֶן.",
            transliteration="Барух Ата Адонай, Элоhэйну Мэлэх hаолам, борэ при hагафэн.",
            translation_ru="Благословен Ты, Господь, Бог наш, Царь вселенной, сотворивший плод виноградной лозы.",
            description="A blessing over wine or grape juice, recited during Kiddush on Shabbat and holidays to sanctify the day.",
            audio_url="/audio/kiddush.mp3",
            order_index=5,
        ),
        Prayer(
            category="Shabbat",
            name_en="Lecha Dodi",
            name_he="לְכָה דוֹדִי",
            text_hebrew="לְכָה דוֹדִי לִקְרַאת כַּלָּה, פְּנֵי שַׁבָּת נְקַבְּלָה.",
            transliteration="Лэха доди ликрат кала, пнэй Шабат нэкабла.",
            translation_ru="Выйди, мой друг, навстречу невесте, встретим лик Субботы.",
            description="A liturgical song sung on Friday evening to welcome Shabbat. Composed by Rabbi Shlomo Alkabetz in the 16th century in Safed.",
            audio_url="/audio/lecha_dodi.mp3",
            order_index=6,
        ),
        Prayer(
            category="Daily",
            name_en="Birkat Hamazon (Grace After Meals) — Short Version",
            name_he="בִּרְכַּת הַמָּזוֹן",
            text_hebrew="בָּרוּךְ אַתָּה יְהוָה אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, הַזָּן אֶת הָעוֹלָם כֻּלּוֹ בְּטוּבוֹ, בְּחֵן בְּחֶסֶד וּבְרַחֲמִים.",
            transliteration="Барух Ата Адонай, Элоhэйну Мэлэх hаолам, hазан эт hаолам куло бэтуво, бэхэн бэхэсэд увэрахамим.",
            translation_ru="Благословен Ты, Господь, Бог наш, Царь вселенной, питающий весь мир по благости Своей, по милости и милосердию.",
            description="Grace after meals — a prayer of thanksgiving recited after eating a meal that includes bread. This is the first blessing of the full Birkat Hamazon.",
            audio_url="/audio/birkat_hamazon.mp3",
            order_index=7,
        ),
    ]

    db.add_all(prayers)
    db.commit()
    db.close()


if __name__ == "__main__":
    seed()
