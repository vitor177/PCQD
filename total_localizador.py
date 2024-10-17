from utils import encontrar_indices

def total_localizador(header):
    # %%
    # %%
    cols_vetor_completo = [
    "timestamp", "temp_avg", "temp_max", "temp_min", "temp_std",
    "ur_avg", "ur_max", "ur_min", "ur_std",
    "pres_avg", "pres_max", "pres_min", "pres_std",
    "prec_tot", "vel_avg", "vel_max", "vel_min", "vel_std",
    "dir_avg", "dir_max", "dir_min", "dir_std",
    "ghi1_avg", "ghi1_max", "ghi1_min", "ghi1_std",
    "ghi2_avg", "ghi2_max", "ghi2_min", "ghi2_std",
    "ghi3_avg", "ghi3_max", "ghi3_min", "ghi3_std",
    "poa_avg", "poa_max", "poa_min", "poa_std",
    "gri1_avg", "gri1_max", "gri1_min", "gri1_std",
    "gri2_avg", "gri2_max", "gri2_min", "gri2_std",
    "dhi_avg", "dhi_max", "dhi_min", "dhi_std",
    "bni_avg", "bni_max", "bni_min", "bni_std",
    "temp_bni", "res_bni",
    "lwdn_avg", "lwdn_std", "lwdn_max", "lwdn_min",
    "lwup_avg", "lwup_std", "lwup_max", "lwup_min",
    "old_avg", "old_std", "old_max", "old_min",
    "temp_old", "res_old",
    "clear_sky_ghi", "clear_sky_bhi", "clear_sky_dhi", "clear_sky_bni",
    "ghi_cams", "bhi_cams", "dhi_cams", "bni_cams"
    ]
    cols_temp = ["temp_avg", "temp_max", "temp_min", "temp_std"]
    cols_ur = ["ur_avg", "ur_max", "ur_min", "ur_std"]
    cols_press = ["pres_avg", "pres_max", "pres_min", "pres_std"]
    cols_prec = ["prec_tot"]
    cols_vel = ["vel_avg", "vel_max", "vel_min", "vel_std"]
    cols_dir = ["dir_avg", "dir_max", "dir_min", "dir_std"]
    cols_ghi1 = ["ghi1_avg", "ghi1_max", "ghi1_min", "ghi1_std"]
    cols_ghi2 = ["ghi2_avg", "ghi2_max", "ghi2_min", "ghi2_std"]
    cols_ghi3 = ["ghi3_avg", "ghi3_max", "ghi3_min", "ghi3_std"]
    cols_poa = ["poa_avg", "poa_max", "poa_min", "poa_std"]
    cols_gri1 = ["gri1_avg", "gri1_max", "gri1_min", "gri1_std"]
    cols_gri2 = ["gri2_avg", "gri2_max", "gri2_min", "gri2_std"]
    cols_dhi = ["dhi_avg", "dhi_max", "dhi_min", "dhi_std"]
    cols_bni = ["bni_avg", "bni_max", "bni_min", "bni_std"]
    cols_lwdn = ["lwdn_avg", "lwdn_max", "lwdn_min", "lwdn_std"]
    cols_lwup = ["lwup_avg", "lwup_max", "lwup_min", "lwup_std"]
    cols_clear_sky = ["clear sky ghi", "clear sky bhi", "clear sky dhi", "clear sky bni", 
                    "ghi", "bhi", "dhi", "bni"]

    vetor_completo = encontrar_indices(cols_vetor_completo, header.columns)
    temp = encontrar_indices(cols_temp, header.columns)
    ur = encontrar_indices(cols_ur, header.columns)
    press = encontrar_indices(cols_press, header.columns)
    prec = encontrar_indices(cols_prec, header.columns)
    vel = encontrar_indices(cols_vel, header.columns)
    dire = encontrar_indices(cols_dir, header.columns)
    ghi1 = encontrar_indices(cols_ghi1, header.columns)
    ghi2 = encontrar_indices(cols_ghi2, header.columns)
    ghi3 = encontrar_indices(cols_ghi3, header.columns)
    poa = encontrar_indices(cols_poa, header.columns)
    gri1 = encontrar_indices(cols_gri1, header.columns)
    gri2 = encontrar_indices(cols_gri2, header.columns)
    dhi = encontrar_indices(cols_dhi, header.columns)
    bni = encontrar_indices(cols_bni, header.columns)
    lwdn = encontrar_indices(cols_lwdn, header.columns)
    lwup = encontrar_indices(cols_lwup, header.columns)
    clear_sky = encontrar_indices(cols_clear_sky, header.columns)

    return vetor_completo, temp, ur, press, prec, vel, dire, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, lwdn, lwup, clear_sky