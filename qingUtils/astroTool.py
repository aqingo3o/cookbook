from astropy.io import fits
from astropy import units

'''# 快速存檔芝士: saveFITS()
# from my github: Hello_circinus/miniscripts
the_file_name (str) :
    就是新檔案的名字，不需要包含副檔名(.fits)
ima_data :
    就是你的內餡, hdul[n].data 的那部分
ref_header :
    整個 header 的湯底, new header 是複製一個已知 header 的大部分...
    需要包含正確的座標資訊！
    所以新存的檔案的 header 有些欄位是不對ㄉ
ref_beam :
    束寬資訊參考源，可以是 radio-beam.Beam()的Beam, 或是 header
beam_a_Beam (bool) : 
    輸進去的 ref_beam 是不是 radio-beam.Beam() 意義上的 beam?
    是的話說是，填入布林值
'''
def saveFITS(the_file_name, ima_data, ref_header, ref_beam, beam_a_Beam):
    the_file_name = the_file_name + '.fits'
    the_header = ref_header.copy() # new header 是複製一個已知 header 的大部分...
    if beam_a_Beam == True: # ref_beam 是實際意義上的 Beam 的話
        the_header['BMAJ'] = ref_beam.major.to(units.deg).value
        the_header['BMIN'] = ref_beam.minor.to(units.deg).value
        the_header['BPA'] = ref_beam.pa.to(units.deg).value
    else: # ref_beam 是一個 header 的話
        the_header['BMAJ'] = ref_beam['BMAJ']
        the_header['BMIN'] = ref_beam['BMAJ']
        the_header['BPA'] = ref_beam['BMAJ']
    fits.writeto(the_file_name, ima_data, the_header, overwrite=True)
    print(f'Successfully saved a new FITS file as {the_file_name}.')

