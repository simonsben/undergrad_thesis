from numpy import zeros, multiply


def run_polya(network, steps=250, trials=10):
    print('Running ' + str(trials) + ' trials.')
    trial_exposures = zeros(steps + 1)

    for i in range(trials):
        network.run_n_steps(steps)
        trial_exposures += multiply(network.trial_exposure, 1/trials)
        network.clear_network()
        print(str((i+1) / trials * 100) + ' complete')

    return trial_exposures
