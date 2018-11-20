from model.network import network
import matplotlib.pyplot as plt
from numpy import mean

num_trials = 50
exposures = []

for i in range(num_trials):
    net = network(100)
    net.run_n_steps(1000)

    exposures.append(net.exposures)
    print('Run', (i+1), 'done,', round((i+1)/num_trials*100), '% complete.')
print('Simulation done.')

plt.figure('Exposure over trials')
for i, run in enumerate(exposures):
    plt.plot(run, label=('Run ' + str(i)), alpha=.5)

mean_exp = mean(exposures, axis=0)
plt.plot(mean_exp, label='Average run')
plt.title('Exposure over runs')
plt.show()
