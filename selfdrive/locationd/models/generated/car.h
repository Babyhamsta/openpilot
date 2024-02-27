#pragma once
#include "rednose/helpers/ekf.h"
extern "C" {
void car_update_25(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_24(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_30(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_26(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_27(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_29(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_28(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_update_31(double *in_x, double *in_P, double *in_z, double *in_R, double *in_ea);
void car_err_fun(double *nom_x, double *delta_x, double *out_1824182802893165637);
void car_inv_err_fun(double *nom_x, double *true_x, double *out_3001419909996988082);
void car_H_mod_fun(double *state, double *out_6171607466300613990);
void car_f_fun(double *state, double dt, double *out_8585209332263716582);
void car_F_fun(double *state, double dt, double *out_8718038346922471479);
void car_h_25(double *state, double *unused, double *out_7258958142503606886);
void car_H_25(double *state, double *unused, double *out_2986591025390143295);
void car_h_24(double *state, double *unused, double *out_5139414876818287246);
void car_H_24(double *state, double *unused, double *out_1759918301576365739);
void car_h_30(double *state, double *unused, double *out_5543721100721544873);
void car_H_30(double *state, double *unused, double *out_5504923983897391922);
void car_h_26(double *state, double *unused, double *out_5253677799676672401);
void car_H_26(double *state, double *unused, double *out_754912293483912929);
void car_h_27(double *state, double *unused, double *out_6762425015907713197);
void car_H_27(double *state, double *unused, double *out_682488766446478314);
void car_h_29(double *state, double *unused, double *out_4497366153343780090);
void car_H_29(double *state, double *unused, double *out_1030873960423072719);
void car_h_28(double *state, double *unused, double *out_9079913736993140768);
void car_H_28(double *state, double *unused, double *out_932756311142253532);
void car_h_31(double *state, double *unused, double *out_6472381714862840725);
void car_H_31(double *state, double *unused, double *out_3017236987267103723);
void car_predict(double *in_x, double *in_P, double *in_Q, double dt);
void car_set_mass(double x);
void car_set_rotational_inertia(double x);
void car_set_center_to_front(double x);
void car_set_center_to_rear(double x);
void car_set_stiffness_front(double x);
void car_set_stiffness_rear(double x);
}