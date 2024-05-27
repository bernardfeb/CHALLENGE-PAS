print ( "<<\t\t NILAI AKHIR SEMESTER \t\t>>" )

pts = int ( input( "Masukkan Nilai PTS : " ) )
pas = int ( input( "Masukkan Nilai PAS : " ) )

nilai_akhir = (0.40 * pts) + (0.60 * pas)

print( f"NILAI AKHIR = { nilai_akhir }" )
if nilai_akhir == 100:
    print ( "<<<    SEMPURNA    >>>")