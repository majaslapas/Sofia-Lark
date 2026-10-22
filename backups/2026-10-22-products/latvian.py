# Latvian titles and descriptions for the products that were still in English (2026-10-22).
# The English originals are in english.json next to this file. Facts are written as
# "Label: value" lines so the product page reads them into its fact rows.
L = {}

def add(handle, title, facts, *story):
    rows = '<br>'.join(f'<strong>{k}:</strong> {v}' for k, v in facts)
    body = f'<p>{rows}</p>' if facts else ''
    body += ''.join(f'<p>{s}</p>' for s in story)
    L[handle] = {'title': title, 'body_html': body}

WATER = 'Nemaina krāsu saskarē ar ūdeni.'
STEEL = 'juveliertērauds'
GSTEEL = 'zeltīts juveliertērauds'
GBRASS = 'misiņš ar 14 karātu zeltījumu'

add('dionysus', 'Dionysus auskari',
    [('Materiāls', GSTEEL)],
    f'{WATER} Hipoalerģiski.',
    'Mītiska greznība tavai rotu kolekcijai. Izturīgi juveliertērauda auskari, kas piešķir tēlam dievišķu eleganci gan īpašos svētkos, gan ikdienā.')

add('isreala-earrings-copy', 'Mara auskari',
    [('Izmērs', '3,5 × 8 cm'), ('Materiāls', 'juveliertērauds, emalja'), ('Akmeņi', 'dabīgie akmeņi')],
    'Mara auskari ir drosmīga un mistiska rota, ko iedvesmojusi acs kā sargājošs simbols. Košas emaljas detaļas un dabīgie akmeņi, kas viegli šūpojas, veido izteiksmīgu akcentu gan ikdienai, gan svētkiem.')

add('b7450', 'Isreala auskari',
    [('Izmērs', '3,2 × 7,2 cm'), ('Materiāls', 'juveliertērauds, emalja'), ('Akmeņi', 'dabīgie akmeņi')],
    'Isreala auskarus iedvesmojusi acs spēcīgā simbolika. Acs forma ar košu emalju un dabīgiem akmeņiem, kas karājas smalkās ķēdītēs, rada noslēpumainu un elegantu akcentu jebkuram tērpam.')

add('b7351', 'Isis auskari',
    [('Izmērs', '0,8 × 1,3 cm'), ('Materiāls', 'misiņš'), ('Akmeņi', 'saldūdens pērles')],
    'Elegance vienkāršībā: misiņa auskari ar smalku saldūdens pērles lāsi un mazu mirdzošu kristāla zvaigznīti augšpusē. Klasiska rota, kas der gan ikdienai, gan īpašiem brīžiem.')

add('b6799', 'Gaija auskari',
    [('Izmērs', '3 × 8 cm'), ('Materiāls', 'nerūsējošais tērauds'), ('Akmeņi', 'kristāli')],
    'Gaija auskari staro greznību: faktūraina zelta krāsas augšdaļa un mirdzošu kristālu rinda, kas krīt kā bārkstis. Izteiksmīga rota, kas piešķir mirdzumu gan ikdienas, gan svētku tērpam.')

add('b6654', 'Selena auskari',
    [('Izmērs', '1,5 × 8 cm'), ('Materiāls', 'nerūsējošais tērauds')],
    'Selena auskari no Paula kolekcijas ir smalku un sievišķīgu būtņu iedvesmoti. Bārkstis šūpojas līdz ar katru kustību, un izsmalcinātā faktūra piešķir tēlam graciozu šarmu.')

add('kokete-earrings-copy', 'Zeltaini viļņoti auskari',
    [('Izmērs', '1,3 × 2 cm'), ('Materiāls', 'nerūsējošais tērauds')],
    'Gluda, viļņota forma ar spīdīgu zelta krāsas apdari, kas tver gaismu un iedzīvina tēlu. Vienkārši, bet pamanāmi auskari ikdienai un svētkiem.')

add('star-drops', 'Zvaigžņu lāšu auskari',
    [('Izmērs', '0,8 × 1,5 cm'), ('Materiāls', 'bronza'), ('Akmeņi', 'kristāli')],
    'Eleganti lāses formas auskari no bronzas, rotāti ar mirdzošiem kristāliem, kas tver gaismu katrā kustībā. Smalks mirdzums gan ikdienai, gan vakaram.')

add('star-heart', 'Zvaigžņu sirds auskari',
    [('Izmērs', '1,5 × 2,8 cm'), ('Materiāls', 'misiņš'), ('Akmeņi', 'kristāli')],
    'Divu lodīšu auskari zelta krāsā: augšējā lodīte klāta ar mirdzošiem kristāliem, apakšējā – lielāka un gludi spīdīga. Rota, kas tver gaismu un piešķir tēlam greznību gan ikdienā, gan svētkos.')

add('wave-ring-copy', 'Saules akmens gredzens',
    [('Materiāls', 'nerūsējošais tērauds'), ('Izmērs', '17')],
    'Ūdensizturīgs un hipoalerģisks.',
    'Elegants gredzens, ko iedvesmojis dabas spēks un saules siltums. Tas neapsūbē un saglabā spīdumu arī saskarē ar ūdeni, tāpēc piemērots ikdienas valkāšanai.')

add('wave-ring', 'Viļņa gredzens',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '18')],
    'Plūstoša forma, kas atgādina okeāna viļņu kustību. Zelta toņa gredzens ar minimālistisku un savdabīgu dizainu, kas der gan ikdienai, gan svinīgiem brīžiem.')

add('aphrodites-ring', 'Afrodītes gredzens',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '18')],
    'Mīlestības un skaistuma dievietes iedvesmots gredzens: izteiksmīga sirds forma ar zelta apdari. Vienkāršs, bet spilgts dizains ikdienai un brīžiem, kad gribas izcelt savu stilu.')

add('half-flower-earrings', 'Puszieda auskari',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '3 × 6 cm')],
    'Mākslinieciski auskari ar pusziedu formu, kas piešķir tēlam apjomu un kustību. Moderns un drosmīgs akcents ikdienai un īpašiem notikumiem.')

add('b6668', 'Kārdinājuma auskari',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '2,3 × 3,8 cm')],
    'Sievišķīgi ziedu formas auskari ar smalkām detaļām un spīdīgu zelta apdari. Dabas skaistuma iedvesmota rota ikdienai un svētkiem.')

add('estere_earrings', 'Estere auskari',
    [('Materiāls', 'zeltīts misiņš'), ('Krāsa', 'balta'), ('Izmērs', '0,6 × 1,1 cm')],
    'Romantiski auskari ar perlamutra sirsniņu un saldūdens pērli. Mūžīgi elegants stils, kas der gan ikdienai, gan īpašiem brīžiem.')

add('b6969', 'Rīta maiguma auskari',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '3 × 4,5 cm')],
    'Mirdzoši auskari ar sirds formas detaļām, kas atgādina maigu rīta gaismu. Izturīgi un neapsūbē, tāpēc droši valkājami gan ikdienā, gan svētkos.')

add('b5071', 'Eirēnes miera auskari',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '1,7 × 4,6 cm')],
    f'{WATER} Neapsūbē.',
    'Miera un harmonijas auskari, ko iedvesmojusi grieķu dieviete Eirēne. Smalks, bet pamanāms dizains ar zelta apdari ikdienai un īpašiem brīžiem.')

add('b7231-1', 'Zelta ziedlapu auskari',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '1,8 × 2,5 cm')],
    'Smalki zelta krāsas auskari, kuru forma atgādina saules starus. Izturīgi un saglabā spīdumu arī saskarē ar ūdeni – gaišs akcents ikdienai un svētkiem.')

add('b7231', 'Viļņoti riņķa auskari',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '1,1 × 2 cm')],
    'Riņķa auskari ar viļņotu faktūru, kas tver gaismu un piešķir smalku mirdzumu. Hipoalerģiski un ūdensizturīgi, tāpēc saglabā spīdumu ilgi.')

add('b7370-copyb334', 'Trīskāršā mirdzuma auskari',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'sudraba'), ('Izmērs', '2,5 × 2,8 cm')],
    'Eleganti sudraba krāsas auskari ar trīs slāņu dizainu. Hipoalerģiski un ūdensizturīgi, tie saglabā spīdumu arī saskarē ar ūdeni. Mūsdienīgi un vienlaikus mūžīgi.')

add('b7266', 'Zelta ziedu burvības auskari',
    [('Izmērs', '3,2 × 5 cm'), ('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Krāsa', 'zelta')],
    'Ziedu formas auskari, kas piešķir šarmu gan ikdienas, gan svētku tērpam. Hipoalerģiski un ūdensizturīgi, tāpēc ilgi saglabā spīdumu.')

add('b7260', 'Ieva auskari',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '3,6 × 11,4 cm')],
    'Dabas iedvesmoti auskari ar smalkām ķēdītēm, kas plūst lejup kā ziedlapiņas. Hipoalerģiski un ūdensizturīgi – grezns akcents ikdienai un svētkiem.')

add('b7193', 'Ievas rīta auskari',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'dažādi toņi'), ('Izmērs', '2,4 × 11 cm')],
    'Garas, plūstošas ķēdītes, kas graciozi kustas līdz ar katru soli, ar smalku akmeni un zeltīta tērauda detaļām. Neapsūbē un ir hipoalerģiski.')

add('b700', 'Jūras zirdziņa auskari',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '5 × 5 cm')],
    'Plūstoša forma, kas tver jūras eleganci. Hipoalerģiski un ūdensizturīgi auskari, kas neapsūbē – drosmīgs un mūsdienīgs akcents ikdienai un svētkiem.')

add('b7256', 'Nāras prieka auskari',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Izmērs', '4 × 8 cm')],
    'Viļņota forma un faktūra piešķir auskariem kustību un dzīvīgumu. Izturīgi un ūdensizturīgi – rota, kas atspoguļo tavu personību.')

add('swirl-of-luxury-earrings', 'Greznības virpuļa auskari',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Izmērs', '4,4 × 4,3 cm')],
    f'{WATER} Hipoalerģiski.',
    'Zelta zvaigžņu staru auskari, kuros satiekas dabas iedvesma un mūsdienīga elegance. Smalka, bet drosmīga forma ikdienai un svinīgiem brīžiem.')

add('b4485', 'Grācijas virpuļa auskari',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Izmērs', '4 × 6,5 cm')],
    f'{WATER} Hipoalerģiski.',
    'Drosmīgi un izteiksmīgi auskari ar neparastu formu, kas izceļ jebkuru tērpu un ilgi saglabā spīdumu.')

add('golden-wave-charm', 'Zelta viļņa gredzens',
    [('Materiāls', GSTEEL), ('Izmērs', 'regulējams')],
    f'{WATER}',
    'Elegants gredzens ar plūstošu formu un spīdīgu zelta apdari. Ūdensizturīgs un neapsūbē, un regulējamais izmērs ļauj to pielāgot jebkuram pirkstam.')

add('moonlit-arch-ring', 'Mēnessgaismas arkas gredzens',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Izmērs', 'regulējams')],
    'Ūdensizturīgs, neapsūbē.',
    'Mirdzošs un rotaļīgs gredzens, kas piešķir tēlam debešķīgu šarmu. Regulējamais izmērs der jebkuram pirkstam – vakaram vai ikdienai.')

add('ball', 'Zelta lodītes gredzens',
    [('Materiāls', 'zeltīts nerūsējošais tērauds'), ('Izmērs', 'regulējams')],
    'Ūdensizturīgs, neapsūbē.',
    'Mūsdienīgs gredzens: slaida horizontāla josla ar smalku lodīti, kas apvieno izsmalcinātību un drosmi. Izturīgais materiāls neapsūbē arī saskarē ar ūdeni, un regulējamais izmērs ļauj gredzenu pielāgot jebkuram pirkstam.')

add('ring-wave-copy', 'Četrlapu āboliņa gredzens',
    [('Materiāls', GSTEEL), ('Izmērs', 'regulējams')],
    f'{WATER}')

add('dore-necklace', 'Dore kaklarota',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Garums', '42 cm')],
    'Smalka nerūsējošā tērauda ķēdīte ar vienmērīgi izvietotām zelta krāsas pērlītēm.',
    'Bez niķeļa, kadmija un svina, tāpēc hipoalerģiska. Ūdensizturīga un ar laiku neapsūbē – kaklarota gan ikdienai, gan īpašiem brīžiem.')

add('multi-chain-necklace', 'Daudzķēžu kaklarota',
    [('Materiāls', 'nerūsējošais tērauds'), ('Krāsa', 'zelta'), ('Garums', '38 cm + 5 cm pagarinājums')],
    'Vairākas smalkas nerūsējošā tērauda ķēdītes, kas veido izsmalcinātu, slāņotu tēlu.',
    'Bez niķeļa, kadmija un svina, tāpēc hipoalerģiska. Ūdensizturīga un ar laiku neapsūbē – kaklarota jebkuram gadījumam.')

add('hoop-earrings-3', 'Kalti riņķa auskari',
    [('Izmērs', '25 × 25 mm, biezums 9 mm'), ('Materiāls', 'nerūsējošais tērauds')],
    'Biezi, kalti pusriņķa auskari ar izteiksmīgu faktūru – drosmīgs akcents, kas tomēr ir ērts valkāšanai visu dienu.',
    'Bez niķeļa, kadmija un svina sāļiem, tāpēc hipoalerģiski. Ūdensizturīgi un ar laiku neapsūbē.')

add('larissa-chip-earrings-copy', 'Pesca riņķa auskari',
    [('Izmērs', '34 × 41 mm, biezums 10 mm'), ('Materiāls', 'nerūsējošais tērauds')],
    'Noapaļotas ovālas formas riņķa auskari ar mūsdienīgu eleganci – daudzpusīga rota ikdienai un svētkiem.',
    'Bez niķeļa, kadmija un svina sāļiem, tāpēc hipoalerģiski. Ūdensizturīgi un ar laiku neapsūbē.')

add('golden-clover-earrings-b7057', 'Zelta āboliņa auskari',
    [('Izmērs', '3,5 × 3,5 cm'), ('Krāsa', 'zelta')],
    'Āboliņa formas auskari ar greznu zelta apdari – romantiskai, mūsdienīgai sievietei, kurai patīk būt pamanītai. Pietiekami izteiksmīgi, lai izceltos, bet nepārspīlēti, gan svētkiem, gan ikdienai.')

add('bouquet-of-golden-flowers', 'Zelta ziedu pušķa auskari',
    [('Materiāls', 'zeltīts juveliertērauds'), ('Izmērs', '4 × 4 cm')],
    f'{WATER}',
    'Auskari kā smalks zelta ziedu pušķis – dabas elegance un mūsdienīgs izsmalcinātums vienā rotā. Viegli, tāpēc ērti valkājami visu dienu vai vakaru. Lieliska dāvana tuvam cilvēkam vai sev.')

add('aproce-24-3', 'Homēra horizonta aproce',
    [('Pārklājums', 'zeltījums')],
    'Daudzpusīga aproce, kas lieliski izskatās viena vai kopā ar citām aprocēm. Tiem, kam patīk kombinēt un veidot savu stilu.')

add('copy-of-pink-tourmaline-decorated-heart-earrings', 'Oniksa pušķa auskari',
    [('Materiāls', 'juveliertērauds'), ('Akmeņi', 'onikss'), ('Izmērs', '3 × 7,5 cm')],
    f'{WATER}')

add('copy-of-golden-textured-clouds-earrings', 'Zelta mākoņu auskari II',
    [('Materiāls', STEEL), ('Izmērs', '2,3 × 5 cm')],
    f'{WATER}')

add('golden-textured-clouds-earrings', 'Zelta mākoņu auskari',
    [('Materiāls', STEEL), ('Izmērs', '2,1 × 6,5 cm')],
    f'{WATER}')

add('double-hoop-golden-circle-earrings', 'Divu zelta loku auskari',
    [('Materiāls', STEEL), ('Izmērs', '3,2 × 5,3 cm')],
    f'{WATER}')

add('rhinestone-palm-leaf-earrings', 'Palmas lapas auskari ar kristāliem',
    [('Materiāls', STEEL), ('Izmērs', '65 × 20 mm')],
    f'{WATER}')

add('modernist-auskari-24-19', 'Prizmas lāšu auskari',
    [('Materiāls', '14 karātu zeltījums'), ('Akmeņi', 'dabīgie dārgakmeņi, kaķacs kristāli'), ('Garums', '65 mm'), ('Platums', '18 mm')],
    'Krāsains akcents jebkuram tērpam: izteiksmīgi auskari ar pērlītēm spilgtos toņos.')

add('earrings-euterpe-1', 'Euterpe auskari ar pērlēm',
    [('Materiāls', GBRASS), ('Akmeņi', 'dabīgās pērles'), ('Garums', '39 mm'), ('Platums', '16 mm')])

add('sarkana-silimanita-papardes', 'Papardes auskari',
    [('Materiāls', GBRASS), ('Garums', '56 mm'), ('Platums', '38 mm')],
    'Lieli, izteiksmīgi auskari ar oriģinālu dizainu – elegance un mākslinieciskums vienā rotā.')

add('bold', 'Bold auskari',
    [('Izmērs', '3 × 7,3 cm'), ('Materiāls', 'nerūsējošais tērauds'), ('Akmeņi', 'kristāli')],
    'Auskari tiem, kas grib būt pamanīti: savdabīga ģeometriska forma ar mirdzošiem kristāliem vakaram vai īpašam notikumam. Hipoalerģiski, tāpēc piemēroti jutīgai ādai, un neapsūbē, saglabājot spīdumu.')

add('earrings-euterpe', 'Euterpe auskari ar pērlēm un kvarcu',
    [('Materiāls', GBRASS), ('Akmeņi', 'dabīgās pērles un kvarcs'), ('Garums', '40 mm'), ('Platums', '22 mm')])

add('earrings-siren', 'Sirēnas auskari',
    [('Materiāls', GBRASS)])

add('earrings-calypso', 'Calypso auskari',
    [('Materiāls', '14 karātu zeltījums'), ('Akmeņi', 'dabīgās pērles vai kristāli'), ('Garums', '61 mm'), ('Platums', '14 mm')],
    'Jūras skaistums tavā tēlā: auskari ar 14 karātu zeltījumu un dabīgām pērlēm vai zaļu silimanītu un krāsainiem kristāliem pēc izvēles.')

add('earrings-olympic-palm', 'Olimpa palmas auskari',
    [('Materiāls', '14 karātu zeltījums'), ('Akmeņi', 'dabīgās pērles')])

add('naudinas', 'Trojas monētu auskari',
    [('Materiāls', GBRASS), ('Garums', '50 mm'), ('Platums', '34 mm')])

add('la-radorita-paparde', 'Labradorīta papardes auskari',
    [('Materiāls', GBRASS), ('Akmeņi', 'dabīgs kristāls')])

add('lauvas-ar-kristaliem', 'Kristāla lauvas auskari',
    [('Materiāls', GBRASS), ('Akmeņi', 'dabīgs kristāls'), ('Garums', '48 mm'), ('Platums', '19 mm')])

add('labradorita-lauvas', 'Tumšās lauvas auskari',
    [('Materiāls', GBRASS), ('Garums', '48 mm'), ('Platums', '19 mm')])

if __name__ == '__main__':
    import json
    json.dump(L, open('latvian.json', 'w'), ensure_ascii=False, indent=1)
    print(len(L))
