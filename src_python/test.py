# print('Beginning test script')
#
# # Imports --------------------------------------------------------------------------------------------------------------
#
# try:
#     import cnv_data, cnv_eval
# except ImportError:
#     print('Unable to import cnv_data')
#
# # Parameters -----------------------------------------------------------------------------------------------------------
#
# # TRACKING_FILE = '..\\data\\tracking\\par2024Cam1\\cam1par2024.txt'
# # LABEL_FILE = '..\\data\\labels\\p2024cam1.dat'
# # cnv_data.load(TRACKING_FILE, LABEL_FILE, behaviour_fields=['smile'])
#
# # TIMESTEPS = 1  # Keep in mind that n_seqs = int(seq_len / TIMESTEPS)
# # BATCH_SZ = 10  # Optionally can set batch_size in fitting/evaluation to number of sequences (n_seqs for all sequences)
# # N_EPOCHS = 10
# # VALIDATION_SPLIT = 0.2
#
# # # Layer params
# # UNITS_N_MIN = 2
# # UNITS_N_MAX = 4
# # H_LAYERS_N_MIN = 1
# # H_LAYERS_N_MAX = 4
# # # Functions
# # # INPUT_FUNCTION = 'relu'
# # HIDDEN_ACT_FUNC = 'relu'
# # OUTPUT_FUNCTION = 'softmax'
#
#
# # Load data ------------------------------------------------------------------------------------------------------------
#
# # # Load files
# # predictors, labels = None, None
# # try:
# #     (predictors, labels) = (cnv_data.load(TRACKING_FILE, LABEL_FILE, behaviour_fields={'smile'}, structured=True))
# # except IOError:
# #     print('Failed to open files')
# # print('Loaded files')
# #
# # # print(predictors.shape)
# # # print(labels.shape)
# #
# # predictors = cnv_data.to_subseqs(predictors, TIMESTEPS)
# # labels = cnv_data.to_subseqs(labels, TIMESTEPS)
# # # print('Split data into subsequences')
#
# # print(predictors.shape)
# # print(labels.shape)
#
#
# # Set up nn_models --------------------------------------------------------------------------------------------------------
#
# # First index of shape is the number of subsequences, second is length of subsequences, third is dimensions of data
#
# # input_dim = predictors.shape[2]
# # output_dim = labels.shape[2]
# # print(input_dim)
# # print(output_dim)
#
# # input_dim = 1
# # output_dim = 1
#
# # input_shape = (TIMESTEPS, input_dim)
#
# # # There is a keras bug where the shape elements are converted to float, caused a tensorflow error
# # print(type(TIMESTEPS))
# # print(type(input_dim))
#
# # Model 1 --------------------------------------------------------------------------------------------------------------
#
# # # Temp for convenience
# # # Can also set recurrent activation and dropout
# # def mk_LSTM_model(input_shape, layer_width, n_hidden_layers, hidden_activation, output_dim, output_func):
# #     mdl = Sequential()
# #     # Input
# #     mdl.add(LSTM(layer_width, return_sequences=True, input_shape=input_shape))
# #     # Hidden
# #     for layer_no in range(0, n_hidden_layers):
# #         mdl.add(LSTM(layer_width, return_sequences=True, activation=hidden_activation))
# #     # Output
# #     mdl.add(LSTM(output_dim, return_sequences=True, activation=output_func))
# #     # Compile
# #     mdl.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
# #     return mdl
# #
# # nn_models = []
# #
# # from math import log
# #
# # for hidden_layers_exp in range(H_LAYERS_N_MIN, int(log(H_LAYERS_N_MAX, 2)) + 1):
# #     for units_exp in range(UNITS_N_MIN, int(log(UNITS_N_MAX, 2))+1):
# #         nn_models.append(mk_LSTM_model(
# #             input_shape=input_shape,
# #             layer_width=2**units_exp,
# #             n_hidden_layers=2**hidden_layers_exp,
# #             hidden_activation=HIDDEN_ACT_FUNC,
# #             output_dim=output_dim,
# #             output_func=OUTPUT_FUNCTION
# #         ))
# #     # units
# # # hidden layers
#
# # model_1 = Sequential()
# # # Input layer
# # model_1.add(LSTM(UNITS_N_MIN,
# #                  return_sequences=True,
# #                  input_shape=input_shape))
# # # Hidden layer(s)
# # for units_exp in range(0, H_LAYERS_N_MIN):
# #     model_1.add(LSTM(UNITS_N_MIN,
# #                      return_sequences=True))
# # # Output layer
# # model_1.add(LSTM(output_dim,
# #                  return_sequences=True,
# #                  activation=OUTPUT_FUNCTION))
# # # Compile
# # print(model_1.summary())
# # model_1.compile(optimizer='rmsprop',
# #                 loss='binary_crossentropy',
# #                 metrics=['accuracy'])
#
# # model_2 = Sequential()
# # # Input layer
# # model_2.add(LSTM(int(UNITS_N_MIN / 2),
# #                  return_sequences=True,
# #                  input_shape=input_shape))
# # # Hidden layer(s)
# # for units_exp in range(0, H_LAYERS_N_MIN*2):
# #     model_2.add(LSTM(int(UNITS_N_MIN / 2),
# #                      return_sequences=True))
# # # Output layer
# # model_2.add(LSTM(output_dim,
# #                  return_sequences=True,
# #                  activation=OUTPUT_FUNCTION))
# # # Compile
# # print(model_2.summary())
# # model_2.compile(optimizer='rmsprop',
# #                 loss='binary_crossentropy',
# #                 metrics=['accuracy'])
#
#
#
# # Train
# # print('Training')
# # model_1.fit(train_predictors, train_labels,
# #           batch_size=BATCH_SZ,
# #           epochs=N_EPOCHS,
# #           validation_split=VALIDATION_SPLIT,
# #           verbose=1)
# # # Can also use batch_size=train_predictors.shape[0]
#
# # # Evaluate
# # print('Evaluating')
# # loss, acc = model_1.evaluate(test_predictors, test_labels,
# #                      batch_size=test_predictors.shape[0],
# #                      verbose=1)  # Accuracy is at index 1, loss at index 0
# # # Can also use batch_size=test_predictors.shape[0]
# # print('\n\bAccuracy: ' + str(acc))
#
#
# # Testing folds --------------------------------------------------------------------------------------------------------
# #
# # # Check exclusivitiy of timestamps
# # n_folds = 5
# # folds = cnv_eval.k_fold(predictors, labels, n_folds=5)
# # for fold_no in range(0, len(folds)):
# #     print('Checking fold number: ' + str(fold_no+1))
# #     fold = folds[fold_no]
# #     train_data, test_data = fold
# #     (train_predictors, train_labels) = train_data
# #     (test_predictors, test_labels) = test_data
# #     train_timestamps = np.unique(train_predictors['timestamp'])
# #     test_timestamps = np.unique(test_predictors['timestamp'])
# #     exclusive = not np.any(np.isin(train_timestamps, test_timestamps))
# #     # Can also assert exclusive
# #     print('Fold is exclusive') if exclusive else print('TEST FAILED: FOLD IS NOT EXCLUSIVE')
# #
# # # Outputs via field indexing
# # n_folds = 5
# # folds = cnv_eval.k_fold(predictors, labels, n_folds=5)
# # for fold_no in range(0, 1):
# #     print('Fold number:\t' + str(fold_no))
# #     fold = folds[fold_no]
# #     train_data, test_data = fold
# #     (train_predictors, train_labels) = train_data
# #     (test_predictors, test_labels) = test_data
# #     for units_exp in range(0, 5):
# #         print('Test data:\t' + str((test_predictors['timestamp'][units_exp]*30)))
# #         for j in range(0, n_folds-1):
# #             print('Train data:\t' + str((train_predictors['timestamp'][units_exp*(n_folds-1)+j]*30)))
# #
# # # Outputs via index
# # n_folds = 5
# # folds = cnv_eval.k_fold(predictors, labels, n_folds=5)
# # for (train_data, test_data) in folds:
# #     (train_predictors, train_labels) = train_data
# #     (test_predictors, test_labels) = test_data
# #     for units_exp in range(0, 3):
# #         print('Test data:\n' + str(test_predictors[units_exp]))
# #         for j in range(0, n_folds - 1):
# #             print('Train data:\n' + str((train_predictors[units_exp * (n_folds - 1) + j])))
# #
# #
# # Testing model evaluation ---------------------------------------------------------------------------------------------

# small_eval_results = cnv_eval.eval_models(nn_models, predictors, labels, verbose=0)
#
# print(tabulate(small_eval_results, headers='keys'))

# for mdl in nn_models:
#     print(mdl.summary())

try:
    import cnv_model as M
    import cnv_data, cnv_eval
except ImportError:
    print('Unable to import from Conversa')

models = [
    M.MeanModel(),
    M.SVMModel(),
]

subjects = [
    (1001, 1),
    (1005, 1),
    (2001, 1),
    (2002, 1),
    (2006, 1),
    (2010, 1),
    (2017, 1),
    (2024, 1),
]

behavs = {
    'smile',
    'talk',
    'laugh',
}

eval_results = cnv_eval.eval_models_on_subjects(models, subjects, behaviours=behavs)
summary = cnv_eval.summary(eval_results)
print(summary)


# # End of tests ----------------------------------------------------------------------------------------------------------
#
# # Load data and evaluation modules
# try:
#     import cnv_data, cnv_eval
# except ImportError:
#     print('Unable to import cnv_data, cnv_eval')
# from tabulate import tabulate
#
# # Load predictor and label data
# # Predictors are kinematic data, labels are behaviour data
# tracking_file = '..\\data\\tracking\\par2024Cam1\\cam1par2024.txt'
# label_file = '..\\data\\labels\\p2024cam1.dat'
#
# predictors, labels = None, None
# behaviours = ['talk']  # We'll only be looking at the talk behaviour
# try:
#     (predictors, labels) = (cnv_data.load(tracking_file, label_file, behaviours))
# except IOError:
#     print('Failed to open files')
#
# # Run an SVM on predictors and labels, printing some of the data:
#
# # Load the SVM model
# try:
#     from cnv_model import SVMModel
# except ImportError:
#     print('Unable to import from cnv_model')
#
# results = cnv_eval.eval_models([SVMModel()], predictors, labels,
#                                verbose=1)  # If we want to suppress output we can set this to 0
#
# # Now our SVM will train on the data
#
# # We have the evaluation results in the results DataFrame, we can print these out in a table
# print(cnv_eval.summary(results))
#
# print('cnv_tests.py: Completed execution')
