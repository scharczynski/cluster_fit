import sys
from python_data import DataProcessor
from analysis_pipeline import AnalysisPipeline
import json
import os
import util
import cellplot
import matplotlib.pyplot as plt
import numpy as np


def run_script(cell_range):

    # path_to_data = '/Users/stevecharczynski/workspace/data/jay/2nd_file'
    # # path_to_data = "/projectnb/ecog-eeg/stevechar/data/jay"
    # # x = np.full(95, 0)
    # # y = np.full(95, 8000)

    # # trial_lengths = np.array(list(zip(x,y)))
    # # with open('/Users/stevecharczynski/workspace/data/jay/2nd_file/trial_lengths.json', 'w') as f:
    # #     json.dump(trial_lengths.tolist(), f)
    # data_processor = DataProcessor(
    #     path_to_data, cell_range)
    # n = 2
    # solver_params = {
    #     "niter": 2,
    #     "stepsize": 10000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds_smt = {
    #     "sigma": [10, 10000],
    #     "mu": [-1000, 10000],
    #     "tau": [0.0002, 0.10],
    #     "a_1": [10**-7, 0.5],
    #     "a_0": [10**-7, 0.5]
    # }
    # bounds_t = {
    #     "a_1": [0, 1 / n],
    #     "ut": [-1000,10000],
    #     "st": [100, 10000],
    #     "a_0": [10**-10, 1 / n]
    # }
    # bounds_c = {
    #     "a_0": [10**-10, 1 / n]
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "Const", "Time"], 0)
    # # pipeline.set_model_bounds("Time", bounds_t)
    # # pipeline.set_model_bounds("Const", bounds_c)
    # pipeline.set_model_bounds(["Time", "Const"], [bounds_t, bounds_c])
    # pipeline.set_model_x0(["Const", "Time"], [[1e-5], [1e-5, 100, 100, 1e-5]])
    # # pipeline.set_model_bounds("SigmaMuTau", bounds_smt)
    # pipeline.fit_even_odd(solver_params)
    # pipeline.fit_all_models(solver_params=solver_params)
    # pipeline.compare_models("Const", "Time", 0.01)
    # pipeline.compare_even_odd("Const", "Time", 0.01)
    # pipeline.compare_models("Time", "SigmaMuTau", 0.01)

    # path_to_data = '/Users/stevecharczynski/workspace/data/brincat_miller'
    # # path_to_data = "/projectnb/ecog-eeg/stevechar/data/brincat_miller/"
    # time_info = [500, 1750]
    # data_processor = DataProcessor(
    #     path_to_data, cell_range, time_info=time_info)
    # n = 2
    # mean_delta = 0.10 * (time_info[1] - time_info[0])
    # mean_bounds = (
    #     (time_info[0] - mean_delta),
    #     (time_info[1] + mean_delta))
    # solver_params = {
    #     "niter": 100,
    #     "stepsize": 1000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds_smt = {
    #     "sigma": [10, 1000],
    #     "mu": [100, 2300],
    #     "tau": [10, 5000],
    #     "a_1": [10**-7, 0.5],
    #     "a_0": [10**-7, 0.5]
    # }
    # bounds = {
    #     "a_1": [0, 1 / n],
    #     "ut": [mean_bounds[0], mean_bounds[1]],
    #     "st": [10, 1000],
    #     "a_0": [10**-10, 1 / n]
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "SigmaMuTau", "Time"], 0)
    # # pipeline = AnalysisPipeline(cell_range, data_processor, [
    # #                         "Time","SigmaMuTau"], 0)
    # pipeline.set_model_bounds("Time", bounds)
    # pipeline.set_model_bounds("SigmaMuTau", bounds_smt)
    # pipeline.fit_all_models(solver_params=solver_params)
    # pipeline.compare_models("Time", "SigmaMuTau", 0.01)

    # path_to_data = '/Users/stevecharczynski/workspace/data/brincat_miller'
    # # path_to_data = "/projectnb/ecog-eeg/stevechar/data/brincat_miller/"
    # time_info = [500, 1750]
    # data_processor = DataProcessor(
    #     path_to_data, cell_range, time_info=time_info)
    # n = 2
    # mean_delta = 0.10 * (time_info[1] - time_info[0])
    # mean_bounds = (
    #     (time_info[0] - mean_delta),
    #     (time_info[1] + mean_delta))
    # solver_params = {
    #     "niter": 5,
    #     "stepsize": 1000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds_t = {
    #     "a_1": [0, 1 / n],
    #     "ut": [mean_bounds[0], mean_bounds[1]],
    #     "st": [10, 1000],
    #     "a_0": [10**-10, 1 / n]
    # }
    # bounds_c = {
    #     "a_0": [10**-10, 1 / n]
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "Const", "Time"], 0)
    # # pipeline = AnalysisPipeline(cell_range, data_processor, [
    # #                         "Time","SigmaMuTau"], 0)
    # pipeline.set_model_bounds("Time", bounds_t)
    # pipeline.set_model_bounds("Const", bounds_c)
    # pipeline.fit_all_models(solver_params=solver_params)
    # pipeline.compare_models("Const", "Time", 0.01)

    # path_to_data = "/Users/stevecharczynski/workspace/data/salz"
    # path_to_data = "/projectnb/ecog-eeg/stevechar/data/salz"
    # time_info = [1000, 21000]
    # data_processor = DataProcessor(
    #     path_to_data, cell_range, time_info=time_info)
    # n = 2
    # mean_delta = 0.10 * (time_info[1] - time_info[0])
    # mean_bounds = (
    #     (time_info[0] - mean_delta),
    #     (time_info[1] + mean_delta))
    # solver_params = {
    #     "niter": 200,
    #     "stepsize": 1000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds = {
    #     "a_1": [0, 1 / n],
    #     "ut": [mean_bounds[0], mean_bounds[1]],
    #     "st": [10, 50000],
    #     "a_0": [10**-10, 1 / n]
    # }
    # bounds_c = {"a_0": [10**-10, 0.999]}
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "Const", "Time"], 0)
    # pipeline.set_model_bounds("Time", bounds)
    # pipeline.set_model_bounds("Const", bounds_c)
    # pipeline.fit_even_odd(solver_params)
    # pipeline.compare_even_odd("Const", "Time", 0.01)
    # pipeline.fit_all_models(solver_params)
    # pipeline.compare_models("Const", "Time", 0.01)

    # path_to_data = "/Users/stevecharczynski/workspace/data/cromer"
    # # path_to_data = '/projectnb/ecog-eeg/stevechar/data/cromer'
    # # path_to_data = "/usr3/bustaff/scharcz/workspace/cromer/"
    # time_info = [400, 2000]
    # data_processor = DataProcessor(
    #     path_to_data, cell_range, time_info=time_info)
    # n_c = 5
    # solver_params = {
    #     "niter": 1,
    #     "stepsize": 100,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": False,
    # }
    # bounds_cat = {
    #     "ut": [0, 2400],
    #     "st": [10, 5000],
    #     "a_0": [10**-10, 1 / n_c],
    #     "a_1": [10**-10, 1 / n_c],
    #     "a_2": [10**-10, 1 / n_c],
    #     "a_3": [10**-10, 1 / n_c],
    #     "a_4": [10**-10, 1 / n_c]
    # }
    # n_cs = 3
    # bounds_cs = {
    #     "ut": [0, 2400],
    #     "st": [10, 5000],
    #     "a_0": [10**-10, 1 / n_cs],
    #     "a_1": [10**-10, 1 / n_cs],
    #     "a_2": [10**-10, 1 / n_cs],
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "CatSetTime","CatTime"], 0.01)
    # pipeline.set_model_bounds("CatSetTime", bounds_cs)
    # pipeline.set_model_bounds("CatTime", bounds_cat)
    # pipeline.set_model_info("CatSetTime", "pairs", [(1,2), (3,4)])
    # pipeline.fit_all_models(solver_params=solver_params)
    # pipeline.compare_models("CatSetTime", "CatTime", 0.01)
    # pipeline.show_condition_fit("CatTime")
    # pipeline.show_condition_fit("CatSetTime")

    # path_to_data = "/Users/stevecharczynski/workspace/data/kim"
    # path_to_data = "/projectnb/ecog-eeg/stevechar/data/kim"
    # time_info = [0, 4784]
    # data_processor = DataProcessor(
    #     path_to_data, cell_range, time_info=time_info)
    # n = 2
    # swarm_params = {
    #     "phip": 0.5,
    #     "phig": 0.5,
    #     "omega": 0.5,
    #     "minstep": 1e-10,
    #     "minfunc": 1e-10,
    #     "maxiter": 1000
    # }
    # bounds = {
    #     "a_1": [0, 1 / n],
    #     "ut": [-200, 5200],
    #     "st": [10, 10000],
    #     "a_0": [10**-10, 1 / n]
    # }
    # bounds_c = {"a_0": [10**-10, 0.999]}
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "Const", "Time"], 0, swarm_params)
    # pipeline.set_model_bounds("Time", bounds)
    # pipeline.set_model_bounds("Const", bounds_c)
    # pipeline.fit_all_models(1)
    # pipeline.compare_models("Const", "Time", 0.01)

    path_to_data = "/Users/stevecharczynski/workspace/data/cromer"
    # path_to_data =  "/projectnb/ecog-eeg/stevechar/data/cromer"
    # with open(path_to_data+'/number_of_trials.json', 'r') as f:
    #     num = json.load(f)
    # x = np.full(max(num), 400)
    # y = np.full(max(num), 2000)

    # trial_lengths = np.array(list(zip(x,y)))
    # with open(path_to_data+'/trial_lengths.json', 'w') as f:
    #     json.dump(trial_lengths.tolist(), f)
    
    data_processor = DataProcessor(
        path_to_data, cell_range, time_info=[400,2000])
    n_t = 2.
    solver_params = {
        "niter": 250,
        "stepsize": 1000,
        "interval": 10,
        "method": "TNC",
        "use_jac": True,
    }
    bounds = {
        "a_1": [10**-10, 1 / n_t],
        "ut": [0., 2200.],
        "st": [10., 5000.],
        "a_0": [10**-10, 1 / n_t]
    }
    bounds_c = {"a_0": [10**-10, 0.999]}
    pipeline = AnalysisPipeline(cell_range, data_processor, [
                                "Time", "Const"], 0)
    # pipeline.show_rasters()

    pipeline.set_model_bounds("Time", bounds)
    pipeline.set_model_bounds("Const", bounds_c)
    pipeline.set_model_x0("Time", [1e-5, 400, 100, 1e-5])
    pipeline.set_model_x0("Const", [1e-5])
    pipeline.fit_even_odd(solver_params)
    pipeline.compare_even_odd("Const", "Time", 0.01)
    pipeline.fit_all_models(solver_params=solver_params)
    pipeline.compare_models("Const", "Time", 0.01)

    


    # path_to_data = '/Users/stevecharczynski/workspace/data/cromer'
    # # path_to_data = "/usr3/bustaff/scharcz/workspace/cromer/"
    # time_info = [400, 2000]
    # data_processor = DataProcessor(
    #     path_to_data, cell_range, time_info=time_info)
    # n_c = 3
    # swarm_params = {
    #     "phip": 0.5,
    #     "phig": 0.7,
    #     "omega": 0.7,
    #     "minstep": 1e-10,
    #     "minfunc": 1e-10,
    #     "maxiter": 1000
    # }
    # bounds_cat = {
    #     "ut": [0, 2400],
    #     "st": [10, 5000],
    #     "a_0": [10**-10, 1 / n_c],
    #     "a_1": [10**-10, 1 / n_c],
    #     "a_2": [10**-10, 1 / n_c],
    # }
    # n_t = 2
    # bounds_t = {
    #     "a_1": [0, 1 / n_t],
    #     "ut": [0, 2400],
    #     "st": [10, 5000],
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # # bounds_cat = ((0,2400), (10, 5000), (10**-10, 1 / n), (0, 1 / n),(0, 1 / n), (0, 1 / n), (0, 1 / n))
    # # bounds= ((0, 1 / n), (0,2400), (10, 5000), (10**-10, 1 / n))
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "CatSetTime", "Time"], 0, swarm_params)
    # pipeline.set_model_bounds("Time", bounds_t)
    # pipeline.set_model_bounds("CatSetTime", bounds_cat)
    # pipeline.set_model_info("CatSetTime", "pairs", [(1,2), (3,4)])
    # pipeline.fit_all_models(1)
    # pipeline.compare_models("Time", "CatSetTime", 0.01)
    # pipeline.show_condition_fit("CatSetTime")

    # path_to_data = '/Users/stevecharczynski/workspace/rui_fake_cells/mixed_firing'
    # time_info = RegionInfo(0, 2000)
    # data_processor = DataProcessor(
    #     path_to_data, cell_range, time_info=time_info)
    # n = 2
    # bounds = {
    #     "a_1": [0, 1 / n],
    #     "ut": [-500, 2500],
    #     "st": [0.01, 5000],
    #     "a_0": [10**-10, 1 / n]
    # }
    # bounds_c = {"a_0": [10**-10, 0.99]}
    # swarm_params = {
    #     "phip": 0.5,
    #     "phig": 0.5,
    #     "omega": 0.5,
    #     "minstep": 1e-10,
    #     "minfunc": 1e-10,
    #     "maxiter": 1000
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "Const", "Time"], 0, swarm_params)
    # pipeline.set_model_bounds("Time", bounds)
    # pipeline.set_model_bounds("Const", bounds_c)
    # pipeline.fit_all_models(3)
    # pipeline.compare_models("Const", "Time", 0.01)

    # util.collect_data(cell_range, "log_likelihoods")
    # util.collect_data(cell_range, "model_comparisons")
    # util.collect_data(cell_range, "cell_fits")

    # path_to_data = "/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1"
    # # path_to_data =  "/projectnb/ecog-eeg/stevechar/data/cromer"
    # time_info = [0, 3993]
    # data_processor = DataProcessor(
    #     path_to_data, cell_range)
    # n_t = 2.
    # solver_params = {
    #     "niter": 10,
    #     "stepsize": 1000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds_c = {
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # bounds_t = {
    #     "a_1": [10**-10, 1 / n_t],
    #     "ut": [0., 2400.],
    #     "st": [10., 5000.],
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                            "Const", "TimeVariableLength"], 0)

    # pipeline.set_model_bounds("TimeVariableLength", bounds_t)
    # pipeline.set_model_bounds("Const",  {"a_0":[10**-10, 1]})

    # # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/trial_length.json", 'rb') as f:
    # #     trial_length = json.load(f)
    # # pipeline.set_model_info("TimeVariableLength", "trial_length", trial_length)
    # pipeline.fit_all_models(solver_params=solver_params)
    # pipeline.compare_models("Const", "TimeVariableLength", 0.01)

    # path_to_data = "/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1"
    # # path_to_data =  "/projectnb/ecog-eeg/stevechar/data/cromer"
    # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/trial_length.json", 'rb') as f:
    #     trial_length = json.load(f)
    # time_info = list(zip(np.zeros(len(trial_length), dtype=int), trial_length))
    # data_processor = DataProcessor(
    #     path_to_data, cell_range, time_info)
    # n_t = 2.
    # solver_params = {
    #     "niter": 1,
    #     "stepsize": 1000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds_pos = {
    #     "a_1": [10**-10, 1 / n_t],
    #     "ut": [0., 1100.],
    #     "st": [10., 2000.],
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # bounds_t = {
    #     "a_1": [10**-10, 1 / n_t],
    #     "ut": [0., 2400.],
    #     "st": [10., 5000.],
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                            "ConstVariable", "RelPosVariable","AbsPosVariable","TimeVariableLength"], 0)

    # pipeline.set_model_bounds("TimeVariableLength", bounds_t)
    # pipeline.set_model_bounds("AbsPosVariable", bounds_pos)
    # pipeline.set_model_bounds("RelPosVariable", bounds_pos)
    # pipeline.set_model_bounds("ConstVariable",  {"a_0":[10**-10, 1]})


    # pipeline.set_model_info("ConstVariable", "trial_length", trial_length)
    # pipeline.set_model_info("TimeVariableLength", "trial_length", trial_length)
    # pipeline.set_model_info("AbsPosVariable", "trial_length", trial_length)
    # pipeline.set_model_info("RelPosVariable", "trial_length", trial_length)

    # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/x_abs.json", 'rb') as f:
    #     abs_pos = np.array(json.load(f))
    # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/x_rel.json", 'rb') as f:
    #     rel_pos = np.array(json.load(f))
    # pipeline.set_model_info("AbsPosVariable", "abs_pos", abs_pos, True)
    # pipeline.set_model_info("RelPosVariable", "rel_pos", rel_pos, True)
    # pipeline.fit_all_models(solver_params=solver_params)
    # pipeline.compare_models("ConstVariable", "RelPosVariable", 0.01)
    # pipeline.compare_models("ConstVariable", "AbsPosVariable", 0.01)
    # pipeline.compare_models("ConstVariable", "TimeVariableLength", 0.01)

    # path_to_data = "/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1"
    # # path_to_data =  "/projectnb/ecog-eeg/stevechar/data/cromer"
    # # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/trial_length_old.json", 'rb') as f:
    # #     trial_length = json.load(f)
    # # time_info = np.array(list(zip(np.zeros(len(trial_length), dtype=int), trial_length)))
    # # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/trial_length_new.json", 'w') as f:
    # #     json.dump(time_info.tolist(), f)
    # data_processor = DataProcessor(
    #     path_to_data, cell_range)
    # n_t = 2.
    # solver_params = {
    #     "niter": 1,
    #     "stepsize": 1000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds_pos = {
    #     "a_1": [10**-10, 1 / n_t],
    #     "ut": [0., 1100.],
    #     "st": [10., 2000.],
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # bounds_t = {
    #     "a_1": [10**-10, 1 / n_t],
    #     "ut": [0., 2400.],
    #     "st": [10., 5000.],
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                            "ConstVariable", "AbsPosVariable"], 0)

    # pipeline.set_model_bounds("AbsPosVariable", bounds_pos)
    # pipeline.set_model_bounds("ConstVariable",  {"a_0":[10**-10, 1]})

    # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/x_abs.json", 'rb') as f:
    #     abs_pos = np.array(json.load(f))
    # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/x_rel.json", 'rb') as f:
    #     rel_pos = np.array(json.load(f))
    # pipeline.set_model_info("AbsPosVariable", "abs_pos", abs_pos, True)
    # pipeline.fit_all_models(solver_params=solver_params)
    # pipeline.compare_models("ConstVariable", "AbsPosVariable", 0.01)

    # path_to_data = "/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1"
    # # path_to_data =  "/projectnb/ecog-eeg/stevechar/data/cromer"
    # # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/trial_length_old.json", 'rb') as f:
    # #     trial_length = json.load(f)
    # # time_info = np.array(list(zip(np.zeros(len(trial_length), dtype=int), trial_length)))
    # # with open("/Users/stevecharczynski/workspace/data/sheehan/lin_track_s1/trial_length_new.json", 'w') as f:
    # #     json.dump(time_info.tolist(), f)
    # data_processor = DataProcessor(
    #     path_to_data, cell_range)
    # n_t = 2.
    # solver_params = {
    #     "niter": 1,
    #     "stepsize": 1000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds_pos = {
    #     "a_1": [10**-10, 1 / n_t],
    #     "ut": [0., 1100.],
    #     "st": [10., 2000.],
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # bounds_t = {
    #     "a_1": [10**-10, 1 / n_t],
    #     "ut": [0., 2400.],
    #     "st": [10., 5000.],
    #     "a_0": [10**-10, 1 / n_t]
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "ConstVariable", "Const"], 0)

    # pipeline.set_model_bounds("Const", {"a_0":[10**-10, 1]})
    # pipeline.set_model_bounds("ConstVariable",  {"a_0":[10**-10, 1]})

    # pipeline.fit_all_models(solver_params=solver_params)

    # path_to_data = '/Users/stevecharczynski/workspace/data/cromer/'
    # # path_to_data = "/projectnb/ecog-eeg/stevechar/data/brincat_miller/"
    # # x = np.full(95, 0)
    # # y = np.full(95, 8000)

    # # trial_lengths = np.array(list(zip(x,y)))
    # # with open('/Users/stevecharczynski/workspace/data/jay/2nd_file/trial_lengths.json', 'w') as f:
    # #     json.dump(trial_lengths.tolist(), f)
    # data_processor = DataProcessor(
    #     path_to_data, cell_range)
    # n = 2
    # solver_params = {
    #     "niter": 2,
    #     "stepsize": 10000,
    #     "interval": 10,
    #     "method": "TNC",
    #     "use_jac": True,
    # }
    # bounds_smt = {
    #     "sigma": [10, 1000],
    #     "mu": [0, 2200],
    #     "tau": [10, 5000],
    #     "a_1": [10**-7, 0.5],
    #     "a_0": [10**-7, 0.5]
    # }
    # bounds_t = {
    #     "a_1": [0, 1 / n],
    #     "ut": [0,2200],
    #     "st": [10, 1000],
    #     "a_0": [10**-10, 1 / n]
    # }
    # bounds_c = {
    #     "a_0": [10**-10, 1 / n]
    # }
    # pipeline = AnalysisPipeline(cell_range, data_processor, [
    #                             "Const", "Time", "SigmaMuTau"], 0)
    # pipeline.set_model_bounds("Time", bounds_t)
    # pipeline.set_model_bounds("Const", bounds_c)
    # pipeline.set_model_bounds("SigmaMuTau", bounds_smt)
    # pipeline.fit_all_models(solver_params=solver_params)
    # pipeline.compare_models("Const", "Time", 0.01)
    # pipeline.compare_models("Time", "SigmaMuTau", 0.01)



run_script(range(10,12))
if __name__ == "__main__":
    cell_range = sys.argv[-2:]
    cell_range = list(map(int, cell_range))
    cell_range = range(cell_range[0], cell_range[1]+1)
    run_script(cell_range)
