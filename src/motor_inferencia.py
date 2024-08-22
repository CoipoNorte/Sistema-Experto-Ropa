import unicodedata

def normalizar_texto(texto):
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto

def recomendar_ropa(ocasion, clima, presupuesto, estilo):
    ocasion = normalizar_texto(ocasion)
    clima = normalizar_texto(clima)
    presupuesto = normalizar_texto(presupuesto)
    estilo = normalizar_texto(estilo)
    
    recomendaciones = []

    # Combinacion: Formal
    if ocasion == 'formal':
        # Combinacion: Formal Frio
        if clima == 'frio':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Un abrigo sencillo y unos zapatos formales asequibles.')
                    recomendaciones.append('Camisa de vestir y pantalones de lana.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un abrigo de corte moderno y botas elegantes pero económicas.')
                    recomendaciones.append('Camisa slim fit y pantalones de corte recto.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo con chaqueta impermeable y zapatillas robustas.')
                    recomendaciones.append('Camisa técnica y pantalones deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un abrigo de lana con detalles artesanales y botas de cuero.')
                    recomendaciones.append('Camisa bohemia y pantalones cómodos.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de lana de buena calidad y zapatos formales.')
                    recomendaciones.append('Camisa de calidad y corbata elegante.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de lino con diseño contemporáneo y zapatos elegantes.')
                    recomendaciones.append('Camisa slim fit y accesorios modernos.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de calidad con zapatillas formales.')
                    recomendaciones.append('Camisa casual y pantalones chinos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje con detalles bohemios y accesorios únicos.')
                    recomendaciones.append('Camisa de lino y pantalones a juego.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de diseñador con zapatos de cuero premium.')
                    recomendaciones.append('Camisa de seda y accesorios lujosos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de alta costura y zapatos italianos de gama alta.')
                    recomendaciones.append('Camisa de alta calidad y corbata de seda.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas exclusivas.')
                    recomendaciones.append('Camisa técnica de alta gama y pantalones elegantes.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje de diseñador con detalles artesanales.')
                    recomendaciones.append('Camisa bohemia de lujo y accesorios exclusivos.')
        # Combinacion: Formal Templado
        elif clima == 'templado':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje ligero y zapatos formales económicos.')
                    recomendaciones.append('Camisa de algodón y corbata a juego.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de lino moderno y zapatos elegantes.')
                    recomendaciones.append('Camisa de manga corta y zapatos de cuero.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo ligero con zapatillas formales.')
                    recomendaciones.append('Camisa casual y pantalones chinos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje con detalles bohemios y sandalias de cuero.')
                    recomendaciones.append('Camisa de lino y chaleco a juego.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de algodón de buena calidad y zapatos de cuero.')
                    recomendaciones.append('Camisa de vestir y cinturón a juego.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje ligero con diseño moderno y zapatos a juego.')
                    recomendaciones.append('Camisa slim fit y accesorios contemporáneos.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo elegante con zapatillas cómodas.')
                    recomendaciones.append('Camisa técnica y pantalones de calidad.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje ligero con detalles bohemios y accesorios únicos.')
                    recomendaciones.append('Camisa bohemia y pantalones a juego.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de diseñador con zapatos italianos.')
                    recomendaciones.append('Camisa de alta calidad y corbata de seda.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de alta costura con accesorios exclusivos.')
                    recomendaciones.append('Camisa slim fit de lujo y corbata moderna.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas exclusivas.')
                    recomendaciones.append('Camisa técnica de alta gama y pantalones elegantes.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje de diseñador con detalles artesanales.')
                    recomendaciones.append('Camisa bohemia de lujo y accesorios únicos.')
        # Combinacion: Formal Calido
        elif clima == 'calido':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje fresco de colores claros y zapatos formales cómodos.')
                    recomendaciones.append('Camisa ligera y pantalones de lino.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje sin chaqueta y mocasines frescos.')
                    recomendaciones.append('Camisa de manga corta y pantalones cortos elegantes.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo elegante con zapatillas ligeras.')
                    recomendaciones.append('Camisa técnica y pantalones cortos deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje ligero con camisa de lino y sandalias.')
                    recomendaciones.append('Camisa bohemia y pantalones sueltos.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje ligero de lino y zapatos formales ventilados.')
                    recomendaciones.append('Camisa de algodón y corbata ligera.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje fresco con diseño moderno y zapatos ventilados.')
                    recomendaciones.append('Camisa de manga corta y accesorios contemporáneos.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo elegante con zapatillas ligeras.')
                    recomendaciones.append('Camisa técnica y pantalones cortos de calidad.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje ligero con detalles bohemios y sandalias cómodas.')
                    recomendaciones.append('Camisa bohemia y pantalones a juego.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de diseñador sin chaqueta y zapatos de cuero ligeros.')
                    recomendaciones.append('Camisa de seda y accesorios elegantes.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de alta costura sin chaqueta y mocasines exclusivos.')
                    recomendaciones.append('Camisa de manga corta de alta calidad y accesorios modernos.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas exclusivas.')
                    recomendaciones.append('Camisa técnica de alta gama y pantalones elegantes.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje de diseñador con detalles artesanales.')
                    recomendaciones.append('Camisa bohemia de lujo y accesorios únicos.')
    
    # Combinación: Informal
    elif ocasion == 'informal':
        # Combinación: Informal y Frío
        if clima == 'frio':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Un suéter grueso y unos jeans oscuros.')
                    recomendaciones.append('Un abrigo de lana sencillo y bufanda a juego.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una chaqueta de moda y zapatillas con estilo pero accesibles.')
                    recomendaciones.append('Un suéter de diseño y pantalones oscuros.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un chándal cálido con zapatillas robustas.')
                    recomendaciones.append('Un suéter térmico y pantalones deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un suéter de lana artesanal y pantalones de pana.')
                    recomendaciones.append('Un chaleco de lana y bufanda artesanal.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Un suéter de marca y pantalones casuales.')
                    recomendaciones.append('Un abrigo de lana de buena calidad y jeans.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una chaqueta moderna de buena calidad y zapatos de diseño.')
                    recomendaciones.append('Un suéter de marca con pantalones ajustados.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto de ropa deportiva de marca con zapatillas resistentes.')
                    recomendaciones.append('Un suéter térmico y pantalones deportivos de buena calidad.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un suéter de lana de diseño exclusivo y pantalones de pana.')
                    recomendaciones.append('Un abrigo bohemio y bufanda a juego.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un abrigo de diseñador y pantalones de lana.')
                    recomendaciones.append('Un suéter de lana de alta gama y accesorios elegantes.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una chaqueta de diseñador y zapatillas exclusivas.')
                    recomendaciones.append('Un suéter de alta gama y pantalones a juego.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas de marca.')
                    recomendaciones.append('Un suéter térmico de alta calidad y pantalones deportivos exclusivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un abrigo bohemio de diseñador y pantalones de lana.')
                    recomendaciones.append('Un suéter de lana exclusivo y bufanda de alta gama.')
        # Combinación: Informal y Templado
        elif clima == 'templado':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Una camisa de algodón y jeans o pantalones chinos.')
                    recomendaciones.append('Un suéter ligero y pantalones casuales.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta de diseño moderno y zapatillas estilosas.')
                    recomendaciones.append('Una chaqueta ligera y jeans ajustados.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto de ropa deportiva ligera con zapatillas cómodas.')
                    recomendaciones.append('Una sudadera con capucha y pantalones deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camisa suelta y pantalones de lino.')
                    recomendaciones.append('Un chaleco bohemio y pantalones cómodos.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Una camisa de marca y pantalones de algodón de buena calidad.')
                    recomendaciones.append('Un suéter de buena calidad y pantalones chinos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta de diseño exclusivo y chaqueta ligera.')
                    recomendaciones.append('Un conjunto moderno con pantalones y zapatos de marca.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de calidad con zapatillas cómodas.')
                    recomendaciones.append('Un suéter de marca y pantalones deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camisa de lino con diseño bohemio y pantalones a juego.')
                    recomendaciones.append('Un chaleco de marca y pantalones cómodos.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Una camisa de diseñador y pantalones de algodón premium.')
                    recomendaciones.append('Un suéter de alta gama y pantalones chinos exclusivos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta de alta gama y chaqueta de diseñador.')
                    recomendaciones.append('Un conjunto moderno con pantalones a medida y accesorios de lujo.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas exclusivas.')
                    recomendaciones.append('Un suéter de marca premium y pantalones deportivos exclusivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camisa de diseñador con estilo bohemio y pantalones a juego.')
                    recomendaciones.append('Un chaleco bohemio de lujo y pantalones cómodos.')
        # Combinación: Informal y Calido
        elif clima == 'calido':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Una camiseta ligera y pantalones cortos.')
                    recomendaciones.append('Una camisa de manga corta y shorts.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta sin mangas y zapatillas ligeras.')
                    recomendaciones.append('Un conjunto de moda para climas cálidos.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo fresco con zapatillas transpirables.')
                    recomendaciones.append('Una camiseta técnica y pantalones cortos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camiseta de algodón y bermudas de lino.')
                    recomendaciones.append('Una camisa suelta y sandalias.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Una camiseta de marca y shorts de alta calidad.')
                    recomendaciones.append('Una camisa de lino y pantalones cortos a juego.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta de diseño exclusivo y sandalias elegantes.')
                    recomendaciones.append('Un conjunto moderno con pantalones cortos y zapatillas.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de marca con zapatillas transpirables.')
                    recomendaciones.append('Una camiseta técnica y pantalones cortos de calidad.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camiseta bohemia y shorts de lino.')
                    recomendaciones.append('Una camisa suelta de marca y sandalias.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un conjunto ligero de diseñador con sandalias premium.')
                    recomendaciones.append('Una camisa de alta gama y pantalones cortos de lujo.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un conjunto de diseñador con camiseta ligera y zapatillas exclusivas.')
                    recomendaciones.append('Una camisa de manga corta de lujo y pantalones cortos elegantes.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas exclusivas.')
                    recomendaciones.append('Una camiseta técnica de alta gama y pantalones cortos de calidad.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un conjunto bohemio de diseñador con pantalones cortos.')
                    recomendaciones.append('Una camiseta de lujo y sandalias exclusivas.')

    # Combinación: Casual
    elif ocasion == 'casual':
        # Combinación: Casual y Frío
        if clima == 'frio':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Un suéter cómodo y pantalones casuales.')
                    recomendaciones.append('Un abrigo sencillo y un suéter de lana.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un jersey de moda y botas casuales.')
                    recomendaciones.append('Una chaqueta ligera y suéter de diseño.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Una sudadera con capucha y pantalones deportivos.')
                    recomendaciones.append('Un abrigo deportivo y zapatillas cómodas.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un suéter de lana y pantalones de mezclilla.')
                    recomendaciones.append('Un chaleco bohemio y jeans.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Un suéter de lana y pantalones casuales de buena calidad.')
                    recomendaciones.append('Un abrigo casual y un suéter elegante.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un jersey de diseño y botas de calidad.')
                    recomendaciones.append('Una chaqueta moderna y pantalones casuales.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de buena calidad con zapatillas resistentes.')
                    recomendaciones.append('Un suéter térmico y pantalones deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un suéter bohemio de lana y pantalones de mezclilla.')
                    recomendaciones.append('Una chaqueta bohemia y jeans.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un abrigo informal de diseñador y botas premium.')
                    recomendaciones.append('Un suéter de alta gama y pantalones casuales exclusivos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un jersey de diseñador y botas de alta calidad.')
                    recomendaciones.append('Una chaqueta de lujo y pantalones a medida.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas exclusivas.')
                    recomendaciones.append('Un suéter térmico de diseñador y pantalones deportivos premium.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un suéter bohemio de diseñador y pantalones de mezclilla exclusivos.')
                    recomendaciones.append('Un abrigo bohemio de lujo y jeans.')
        # Combinación: Casual y Templado
        elif clima == 'templado':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Una camiseta y jeans cómodos.')
                    recomendaciones.append('Una camisa de algodón y pantalones casuales.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta con estilo y zapatillas casuales.')
                    recomendaciones.append('Una chaqueta ligera y jeans ajustados.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo ligero con zapatillas casuales.')
                    recomendaciones.append('Una camiseta técnica y pantalones deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camiseta y pantalones de lino.')
                    recomendaciones.append('Una camisa bohemia y pantalones cómodos.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Una camisa de marca y pantalones de algodón.')
                    recomendaciones.append('Una camiseta de buena calidad y jeans.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta de diseño y chaqueta ligera.')
                    recomendaciones.append('Un conjunto moderno con pantalones casuales de calidad.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de marca con zapatillas cómodas.')
                    recomendaciones.append('Una camiseta técnica y pantalones de calidad.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camiseta bohemia de marca y pantalones de lino.')
                    recomendaciones.append('Una camisa suelta y pantalones cómodos.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Una camiseta de diseñador y pantalones casuales premium.')
                    recomendaciones.append('Una camisa de alta gama y jeans de lujo.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un conjunto moderno de diseñador con zapatillas exclusivas.')
                    recomendaciones.append('Una camiseta de alta gama y chaqueta de lujo.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas de marca.')
                    recomendaciones.append('Una camiseta técnica premium y pantalones deportivos de diseñador.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camiseta bohemia de diseñador y pantalones a juego.')
                    recomendaciones.append('Una camisa bohemia de lujo y pantalones cómodos.')
        # Combinación: Casual y Calido
        elif clima == 'calido':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Una camiseta ligera y bermudas.')
                    recomendaciones.append('Una camisa de manga corta y pantalones cortos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta sin mangas y shorts modernos.')
                    recomendaciones.append('Una camiseta fresca y sandalias.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo fresco con zapatillas ligeras.')
                    recomendaciones.append('Una camiseta técnica y shorts transpirables.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camiseta de algodón y pantalones cortos.')
                    recomendaciones.append('Una camisa bohemia y sandalias.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Una camiseta de marca y shorts de lino.')
                    recomendaciones.append('Una camisa de calidad y pantalones cortos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Una camiseta de diseño y shorts elegantes.')
                    recomendaciones.append('Un conjunto moderno con sandalias de calidad.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de buena calidad con zapatillas frescas.')
                    recomendaciones.append('Una camiseta técnica y shorts de marca.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camiseta bohemia de marca y pantalones cortos de lino.')
                    recomendaciones.append('Una camisa suelta y sandalias de calidad.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Una camiseta de diseñador y bermudas premium.')
                    recomendaciones.append('Una camisa de alta gama y shorts exclusivos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un conjunto de diseñador con camiseta ligera y shorts de lujo.')
                    recomendaciones.append('Una camiseta de alta gama y sandalias premium.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas exclusivas.')
                    recomendaciones.append('Una camiseta técnica de diseñador y shorts de calidad.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Una camiseta bohemia de lujo y pantalones cortos exclusivos.')
                    recomendaciones.append('Una camisa bohemia de diseñador y sandalias premium.')

    # Combinación: Especial
    elif ocasion == 'especial':
        # Combinación: Especial y Frío
        if clima == 'frio':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de buen corte y abrigo económico.')
                    recomendaciones.append('Un suéter fino y un abrigo sencillo.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje moderno con abrigo de lana.')
                    recomendaciones.append('Un conjunto de lana y una chaqueta de diseño.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo elegante con chaqueta robusta.')
                    recomendaciones.append('Una sudadera elegante y pantalones deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje con detalles bohemios y botas de cuero.')
                    recomendaciones.append('Un suéter bohemio y pantalones de lana.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de lana de buena calidad con un abrigo elegante.')
                    recomendaciones.append('Un abrigo de lana y un traje a medida.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de calidad media con chaqueta de diseño.')
                    recomendaciones.append('Un conjunto moderno con abrigo de buena calidad.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo elegante con chaqueta de calidad.')
                    recomendaciones.append('Una sudadera de marca y pantalones deportivos premium.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje bohemio de calidad con botas de buen diseño.')
                    recomendaciones.append('Una camisa bohemia y un abrigo elegante.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de diseñador con abrigo de alta gama y zapatos premium.')
                    recomendaciones.append('Un traje a medida con un abrigo de lujo.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de diseñador con abrigo de alta gama y zapatos exclusivos.')
                    recomendaciones.append('Un conjunto moderno de alta gama con accesorios de lujo.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de diseñador con chaqueta de lujo.')
                    recomendaciones.append('Una sudadera de alta gama con pantalones deportivos exclusivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje bohemio de diseñador con botas premium.')
                    recomendaciones.append('Una camisa bohemia de alta gama y un abrigo exclusivo.')
        # Combinación: Especial y Templado
        elif clima == 'templado':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje ligero con zapatos formales asequibles.')
                    recomendaciones.append('Una camisa y pantalones de calidad media.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de corte moderno con zapatos de diseñador accesibles.')
                    recomendaciones.append('Una chaqueta moderna y pantalones de buen corte.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo elegante con zapatillas formales.')
                    recomendaciones.append('Una chaqueta deportiva y pantalones elegantes.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje con detalles bohemios y sandalias de cuero.')
                    recomendaciones.append('Una camisa bohemia y pantalones cómodos.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de calidad media con zapatos de cuero.')
                    recomendaciones.append('Una camisa de buena calidad con pantalones elegantes.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de diseño con zapatos de buena calidad.')
                    recomendaciones.append('Un conjunto moderno con accesorios de marca.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de buena calidad con zapatillas elegantes.')
                    recomendaciones.append('Una chaqueta deportiva de calidad con pantalones a juego.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje bohemio con detalles exclusivos y sandalias de calidad.')
                    recomendaciones.append('Una camisa bohemia de buena calidad con pantalones cómodos.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de diseñador con zapatos italianos premium.')
                    recomendaciones.append('Un traje a medida con accesorios exclusivos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de diseñador con zapatos italianos y accesorios de lujo.')
                    recomendaciones.append('Un conjunto moderno de alta gama con todos los detalles.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas de diseñador.')
                    recomendaciones.append('Una chaqueta deportiva de alta gama con pantalones exclusivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje bohemio de diseñador con sandalias premium.')
                    recomendaciones.append('Una camisa bohemia de alta gama y pantalones exclusivos.')
        # Combinación: Especial y Calido
        elif clima == 'calido':
            if presupuesto == 'bajo':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje fresco de colores claros y zapatos formales.')
                    recomendaciones.append('Una camisa ligera con pantalones cortos.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje sin chaqueta y mocasines elegantes.')
                    recomendaciones.append('Una camisa moderna con pantalones cortos elegantes.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo elegante con zapatillas ligeras.')
                    recomendaciones.append('Una camiseta fresca con pantalones deportivos.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje ligero con camisa de lino y sandalias.')
                    recomendaciones.append('Una camisa bohemia con pantalones cortos.')
            elif presupuesto == 'medio':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje ligero de lino con zapatos formales ventilados.')
                    recomendaciones.append('Una camisa de lino con pantalones cortos de calidad.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje ligero de diseño sin chaqueta y mocasines de calidad.')
                    recomendaciones.append('Un conjunto moderno con pantalones cortos y accesorios elegantes.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de buena calidad con zapatillas ligeras.')
                    recomendaciones.append('Una camiseta técnica y shorts transpirables de marca.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje ligero de lino con sandalias de calidad.')
                    recomendaciones.append('Una camisa bohemia de lino con pantalones cortos.')
            elif presupuesto == 'alto':
                if estilo == 'clasico':
                    recomendaciones.append('Un traje de diseñador sin chaqueta y zapatos de cuero ligeros.')
                    recomendaciones.append('Un traje de alta gama con accesorios exclusivos y zapatos premium.')
                elif estilo == 'moderno':
                    recomendaciones.append('Un traje de diseñador sin chaqueta con mocasines de lujo.')
                    recomendaciones.append('Un conjunto moderno de alta gama con todos los detalles.')
                elif estilo == 'deportivo':
                    recomendaciones.append('Un conjunto deportivo de lujo con zapatillas exclusivas.')
                    recomendaciones.append('Una camiseta técnica de diseñador con shorts de calidad.')
                elif estilo == 'bohemio':
                    recomendaciones.append('Un traje bohemio de diseñador con sandalias exclusivas.')
                    recomendaciones.append('Una camisa bohemia de alta gama con pantalones cortos de lujo.')

    # CoipoNota: Deberia seguir agregando?

    if not recomendaciones:
        recomendaciones.append('Lo siento, no tengo una recomendación específica para esta combinación.')

    return recomendaciones
