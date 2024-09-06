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
    yield lats, lons, "gray", "(Planned) Germany, 2024"

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
        "Messel Pit Fossil Site",
        "Mathildenhöhe Darmstadt",
        "Abbey and Altenmünster of Lorsch",
        "Speyer Cathedral",
        "ShUM Sites of Speyer, Worms and Mainz",
        "Maulbronn Monastery Complex",
        "Strasbourg, Grande-Île and <em>Neustadt</em>",
        "Place Stanislas, Place de la Carrière and Place d'Alliance in Nancy",
        "Völklingen Ironworks"
        
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgray", "(Possible) Wallonia"

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
        "The Great Spa Towns of Europe",
        "City of Luxembourg: its Old Quarters and Fortifications",
        "Roman Monuments, Cathedral of St Peter and Church of Our Lady in Trier",
        "Upper Middle Rhine Valley",
        "Castles of Augustusburg and Falkenlust at Brühl",
        "Zollverein Coal Mine Industrial Complex in Essen"
    ]:
        row = df[df['name_en'] == name].reset_index(drop=True)
        assert len(row) == 1, f"length of row is {len(row)}"
        lats.append(row['latitude'][0]); lons.append(row['longitude'][0])
    yield lats, lons, "lightgray", "(Possible) Luxembourg and Ruhr"


