def journey_generator(df):
    lats = []; lons = []
    for name in [
        "Historic Centre of Avignon: Papal Palace, Episcopal Ensemble and Avignon Bridge",
        "Pont du Gard (Roman Aqueduct)",
        "Historic Centre of Avignon: Papal Palace, Episcopal Ensemble and Avignon Bridge",
        "Roman Theatre and its Surroundings and the \"Triumphal Arch\" of Orange",
        "Historic Centre of Avignon: Papal Palace, Episcopal Ensemble and Avignon Bridge",
        "Arles, Roman and Romanesque Monuments",
        "Historic Centre of Avignon: Papal Palace, Episcopal Ensemble and Avignon Bridge",
        "The Maison Carrée of Nîmes",
        "Historic Fortified City of Carcassonne",
        "Canal du Midi",
        "Routes of Santiago de Compostela in France",
        "Episcopal City of Albi"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "purple", "South of France, 2024"

    lats = []; lons = []
    for name in [
        "Historic Centre of Oporto, Luiz I Bridge and Monastery of Serra do Pilar",
        "Monastery of the Hieronymites and Tower of Belém in Lisbon",
        "Cultural Landscape of Sintra"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "yellow", "Portugal, 2023"

    lats = []; lons = []
    for name in [
        "La Grand-Place, Brussels",
        "Stoclet House",
        "Major Town Houses of the Architect Victor Horta (Brussels)",
        "Ancient and Primeval Beech Forests of the Carpathians and Other Regions of Europe",
        "Flemish Béguinages",
        "The Architectural Work of Le Corbusier, an Outstanding Contribution to the Modern Movement"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "yellow", "Portugal, 2023"

    lats = []; lons = []
    for name in [
        "Church and Dominican Convent of Santa Maria delle Grazie with “The Last Supper” by Leonardo da Vinci",
        "City of Verona",
        "The Porticoes of Bologna",
        "Historic Centre of Florence",
        "Vatican City",
        "Historic Centre of Rome, the Properties of the Holy See in that City Enjoying Extraterritorial Rights and San Paolo Fuori le Mura"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "green", "Italy, 2022"

    lats = []; lons = []
    for name in [
        "Jewish-Medieval Heritage of Erfurt",
        "Classical Weimar",
        "Bauhaus and its Sites in Weimar, Dessau and Bernau",
        "Erzgebirge/Krušnohoří Mining Region",
        "Museumsinsel (Museum Island), Berlin",
        "Berlin Modernism Housing Estates",
        "Palaces and Parks of Potsdam and Berlin"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "darkorange", "Germany, 2024"

    lats = []; lons = []
    for name in [
        "The Four Lifts on the Canal du Centre and their Environs, La Louvière and Le Roeulx (Hainaut)",
        "Neolithic Flint Mines at Spiennes (Mons)",
        "Major Mining Sites of Wallonia",
        "Nord-Pas de Calais Mining Basin",
        "Notre-Dame Cathedral in Tournai"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgray", "(Possible) Wallonia"

    lats = []; lons = []
    for name in [
        "Frontiers of the Roman Empire",
        "Messel Pit Fossil Site",
        "Mathildenhöhe Darmstadt",
        "Abbey and Altenmünster of Lorsch",
        "Speyer Cathedral",
        "ShUM Sites of Speyer, Worms and Mainz",
        "Maulbronn Monastery Complex"
        
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightpink", "Germany 2026"

    lats = []; lons = []
    for name in [
        "Historic Centre of Naples",
        "18th-Century Royal Palace at Caserta with the Park, the Aqueduct of Vanvitelli, and the San Leucio Complex",
        "Castel del Monte",
        "The <I>Trulli</I> of Alberobello",
        "The Sassi and the Park of the Rupestrian Churches of Matera",
        "Cilento and Vallo di Diano National Park with the Archeological Sites of Paestum and Velia, and the Certosa di Padula",
        "Costiera Amalfitana",
        "Historic Centre of Naples"
        
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgray", "(Possible) South Italy"

    lats = []; lons = []
    for name in [
        "Arab-Norman Palermo and the Cathedral Churches of Cefalú and Monreale",
        "Isole Eolie (Aeolian Islands)",
        "Mount Etna",
        "Syracuse and the Rocky Necropolis of Pantalica",
        "Late Baroque Towns of the Val di Noto (South-Eastern Sicily)",
        "Villa Romana del Casale",
        "Archaeological Area of Agrigento",
        "Arab-Norman Palermo and the Cathedral Churches of Cefalú and Monreale"  
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgray", "(Possible) Sicily"

    lats = []; lons = []
    for name in [
        "City of Luxembourg: its Old Quarters and Fortifications",
        "Roman Monuments, Cathedral of St Peter and Church of Our Lady in Trier",
        "Upper Middle Rhine Valley",
        "The Great Spa Towns of Europe",
        "Castles of Augustusburg and Falkenlust at Brühl",
        "Cologne Cathedral"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "deeppink", "Luxembourg and Germany, 2025"

    lats = []; lons = []
    for name in [
        "Old Town of Segovia and its Aqueduct",
        "Paseo del Prado and Buen Retiro, a landscape of Arts and Sciences",
        "Historic City of Toledo",
        "Paseo del Prado and Buen Retiro, a landscape of Arts and Sciences",
        "Historic Centre of Cordoba",
        "Cathedral, Alcázar and Archivo de Indias in Seville",
        "Historic Centre of Cordoba",
        "Alhambra, Generalife and Albayzín, Granada",
        "Historic Centre of Cordoba",
        "Caliphate City of Medina Azahara",
        "Historic Centre of Cordoba",
        "Paseo del Prado and Buen Retiro, a landscape of Arts and Sciences",
        "Works of Antoni Gaudí",
        "Palau de la Música Catalana and Hospital de Sant Pau, Barcelona",
        "Historic Site of Lyon"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "aqua", "Spain 2026"

    lats = []; lons = []
    for name in [
        "Historic Centre of Florence",
        "Medici Villas and Gardens in Tuscany",
        "Piazza del Duomo, Pisa",
        "Historic Centre of San Gimignano",
        "Historic Centre of Siena",
        "Val d'Orcia",
        "Historic Centre of the City of Pienza",
        "Historic Centre of Florence"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "crimson", "Tuscany 2026"

    lats = []; lons = []
    for name in [
        "Museumsinsel (Museum Island), Berlin",
        "Muskauer Park / Park Mużakowski",
        "Moravian Church Settlements",
        "Naumburg Cathedral",
        "Collegiate Church, Castle and Old Town of Quedlinburg",
        "Garden Kingdom of Dessau-Wörlitz",
        "Luther Memorials in Eisleben and Wittenberg",
        "Museumsinsel (Museum Island), Berlin"
        
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) East Germany"

    lats = []; lons = []
    for name in [
        "St Mary's Cathedral and St Michael's Church at Hildesheim",
        "Mines of Rammelsberg, Historic Town of Goslar and Upper Harz Water Management System",
        "Fagus Factory in Alfeld",
        "Carolingian Westwork and Civitas Corvey",
        "Bergpark Wilhelmshöhe",
        "Wartburg Castle"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Middle Germany"

    lats = []; lons = []
    for name in [
        "The Climats, terroirs of Burgundy",
        "From the Great Saltworks of Salins-les-Bains to the Royal Saltworks of Arc-et-Senans, the Production of Open-pan Salt",
        "Fortifications of Vauban",
        "The Climats, terroirs of Burgundy",
        "Vézelay, Church and Hill",
        "Cistercian Abbey of Fontenay",
        "The Climats, terroirs of Burgundy"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Burgundy"

    lats = []; lons = []
    for name in [
        "Church and Dominican Convent of Santa Maria delle Grazie with “The Last Supper” by Leonardo da Vinci",
        "Ivrea, industrial city of the 20th century",
        "Residences of the Royal House of Savoy",
        "Vineyard Landscape of Piedmont: Langhe-Roero and Monferrato",
        "Genoa: <i>Le Strade Nuove</i> and the system of the<i> Palazzi dei Rolli</i>",
        "Portovenere, Cinque Terre, and the Islands (Palmaria, Tino and Tinetto)"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) North-Eastern Italy"

    lats = []; lons = []
    for name in [
        "Rhaetian Railway in the Albula / Bernina Landscapes",
        "Rock Drawings in Valcamonica",
        "Longobards in Italy. Places of the Power (568-774 A.D.)",
        "Venetian Works of Defence between the 16th and 17th Centuries: <em>Stato da Terra</em> – Western <em>Stato da Mar</em>",
        "Crespi d'Adda",
        "Monte San Giorgio",
        "<I>Sacri Monti</I> of Piedmont and Lombardy"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Northern Italy"

    lats = []; lons = []
    for name in [
        "Historic Centre of Rome, the Properties of the Holy See in that City Enjoying Extraterritorial Rights and San Paolo Fuori le Mura",
        "Assisi, the Basilica of San Francesco and Other Franciscan Sites",
        "Historic Centre of Urbino",
        "San Marino Historic Centre and Mount Titano",
        "The system of Italian-style <em>condominio</em> theatres of the 18th and 19th centuries in Central Italy",
        "Early Christian Monuments of Ravenna"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Central Italy"

    lats = []; lons = []
    for name in [
        "Nice, Winter Resort Town of the Riviera",
        "Decorated Cave of Pont d’Arc, known as Grotte Chauvet-Pont d’Arc, Ardèche",
        "The Causses and the Cévennes, Mediterranean agro-pastoral Cultural Landscape",
        "Chaîne des Puys - Limagne fault tectonic arena"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Southern France"

    lats = []; lons = []
    for name in [
        "Water Management System of Augsburg",
        "Caves and Ice Age Art in the Swabian Jura",
        "Monastic Island of Reichenau",
        "Prehistoric Pile Dwellings around the Alps",
        "Abbey of St Gall"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Southern Germany"

    lats = []; lons = []
    for name in [
        "Würzburg Residence with the Court Gardens and Residence Square",
        "Town of Bamberg",
        "Margravial Opera House Bayreuth",
        "Old town of Regensburg with Stadtamhof",
        "Pilgrimage Church of Wies",
        "The Palaces of King Ludwig II of Bavaria: Neuschwanstein, Linderhof, Schachen and Herrenchiemsee"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Mid-Southern Germany"

    lats = []; lons = []
    for name in [
        "The Porticoes of Bologna",
        "Ferrara, City of the Renaissance, and its Po Delta",
        "Mantua and Sabbioneta",
        "Evaporitic Karst and Caves of Northern Apennines",
        "Cathedral, Torre Civica and Piazza Grande, Modena",
        "The Porticoes of Bologna"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Emilia-Romagna"

    lats = []; lons = []
    for name in [
        "The Dolomites",
        "Padua’s fourteenth-century fresco cycles",
        "Botanical Garden (Orto Botanico), Padua",
        "Le Colline del Prosecco di Conegliano e Valdobbiadene",
        "Archaeological Area and the Patriarchal Basilica of Aquileia",
        "Venice and its Lagoon"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "(Possible) Emilia-Romagna"

    lats = []; lons = []
    for name in [
        "Bourges Cathedral",
        "Abbey Church of Saint-Savin sur Gartempe",
        "The Loire Valley between Sully-sur-Loire and Chalonnes",
        "Megaliths of Carnac and of the shores of Morbihan",
        "Mont-Saint-Michel and its Bay",
        "Beaches of the D-Day Landings, Normandy, 1944",
        "Le Havre, the City Rebuilt by Auguste Perret"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgrey", "Western France"




