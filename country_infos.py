from countryinfo import CountryInfo

def country_infos(country):

    country_select = CountryInfo(country)
    return f"""País: {country_select.name()}\n
            Capital: {country_select.capital()}\n
            Currencies: {country_select.currencies()}\n
            Languages: {country_select.languages()}\n
            Borders: {country_select.borders()}\n
            Calling codes: {country_select.calling_codes()}\n
            Population: {country_select.population()}
        
        
        """
print(country_infos('Brasil'))
