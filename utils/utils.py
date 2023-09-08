class ImExTariff:
    def __init__(self, _hscode, _fatherhscode, mota, mota_xin, deep):
        self.hscode = _hscode
        self.fatherhscode = _fatherhscode
        self.mota = mota
        self.mota_xin = mota_xin
        self.deep = deep

    def display(self):
        print(f"HS Code: {self.hscode}")
        print(f"Father HS Code: {self.fatherhscode}")
        print(f"Mota: {self.mota}")
        print(f"Mota Xin: {self.mota_xin}")
        print(f"Deep: {self.deep}")


class TariffDatabase:
    def __init__(self):
        self.tariffs = []

    def add_tariff(self, tariff):
        self.tariffs.append(tariff)

    def find_tariff(self, hscode):
        for tariff in self.tariffs:
            if tariff.hscode == hscode:
                return tariff
        return None

    def update_tariff(self, hscode, new_tariff):
        existing_tariff = self.find_tariff(hscode)
        if existing_tariff:
            existing_tariff.hscode = new_tariff.hscode
            existing_tariff.fatherhscode = new_tariff.fatherhscode
            existing_tariff.mota = new_tariff.mota
            existing_tariff.mota_xin = new_tariff.mota_xin
            existing_tariff.deep = new_tariff.deep
            return True
        return False

    def delete_tariff(self, hscode):
        existing_tariff = self.find_tariff(hscode)
        if existing_tariff:
            self.tariffs.remove(existing_tariff)
            return True
        return False

    def get_related_tariffs(self, fatherhscode):
        related_tariffs = []
        for tariff in self.tariffs:
            if tariff.fatherhscode == fatherhscode:
                related_tariffs.append(tariff)
        return related_tariffs

def create_father_hscode(father_list,hscode):
    for item in father_list:
        if item['_fatherhscode'] == "":
            item['_fatherhscode'] = hscode
    return father_list


def gather_father_mota(mota_,father_list):
    result = mota_.lower().replace("loại khác",'').replace("- ",'')
    for item in father_list:
        if item['mota_xin'].lower().replace("loại khác",'').replace("- ",'') not in result:
            result+=" "
            result+=item['mota_xin'].lower().replace("loại khác",'').replace("- ",'')
    return result

def check_max_len(text,checker):
    if len(text) <=len(checker):
        return len(text)
    return len(checker)



