from house_info import HouseInfo:
class EnergyData(HouseInfo):
    ENERGY_PER_BULB=0.2
    ENERGY_BITS=0x0F0
    def _get_energy(self,rec):
        energy=(int(rec,base=16))
        energy=energy and self.ENERGY_BITS
        energy=energy>>4
    def _conver_data(self,data):
        recs=[]
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)




