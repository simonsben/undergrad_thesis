from numpy import zeros, multiply, array, copy


def run_polya(network, steps=101, trials=10, combine=True):
    print('Running ' + str(trials) + ' trials.')
    trial_exposures = zeros(steps + 1) if combine else []

    for i in range(trials):
        network.run_n_steps(steps)
        if combine:
            trial_exposures += multiply(network.trial_exposure, 1/trials)
        else:
            trial_exposures.append(copy(network.trial_exposure))
        network.clear_network()
        print(str((i+1) / trials * 100) + ' complete')

    return trial_exposures if combine else array(trial_exposures)
