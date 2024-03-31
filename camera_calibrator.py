import component.chessboard_calibration as cc
import component.distortion_correction as dc

video_file = 'chessboard.avi'
board_pattern = (10, 7)
board_cellsize = 0.025

img_select = cc.select_img(video_file, board_pattern)
assert len(img_select) > 0, 'There is no selected images!'
rms, K, dist_coeff, rvecs, tvecs = cc.calib_chessboard(img_select, board_pattern, board_cellsize)

# Print calibration results
print('## Camera Calibration Results')
print(f'* The number of selected images = {len(img_select)}')
print(f'* RMS error = {rms}')
print(f'* Camera matrix (K) = \n{K}')
print(f'* Distortion coefficient (k1, k2, p1, p2, k3, ...) = {dist_coeff.flatten()}')

dc.dist_corr(video_file, K, dist_coeff)