""""""  		  	   		 	 	 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	 	 			  		 			     			  	 
All Rights Reserved  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	 	 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 			  		 			     			  	 
or edited.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	 	 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 			  		 			     			  	 
GT honor code violation.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Student Name: Yumna Rizvi 		  	   		 	 	 			  		 			     			  	 
GT User ID: yrizvi3  		  	   		 	 	 			  		 			     			  	 
GT ID: 3953194 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import numpy as np
import matplotlib.pyplot as plt
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def author():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: str  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return "yrizvi3"  # replace tb34 with your Georgia Tech username.
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def gtid():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: int  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return 3953194  # replace with your GT ID number
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 	 	 			  		 			     			  	 
    :type win_prob: float  		  	   		 	 	 			  		 			     			  	 
    :return: The result of the spin.  		  	   		 	 	 			  		 			     			  	 
    :rtype: bool  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    result = False  		  	   		 	 	 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 	 	 			  		 			     			  	 
        result = True  		  	   		 	 	 			  		 			     			  	 
    return result  		  	   		 	 	 			  		 			     			  	 

def test_code():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Method to test your code 	  	   		 	 	 			  		 			     			  	 	 	 	 			  		 			     			  	 
    win_prob = 0.60  # set appropriately to the probability of a win  		  	   		 	 	 			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		 	 	 			  		 			     			  	 
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	 	 			  		 			     			  	 
    # add your code here to implement the experiments  		 	  	   		 	 	 			  		 			     			  	 
    """
    np.random.seed(gtid()) # do this only once
    win_prob = 18 / 38  # set appropriately to the probability of a win
    num_spins = 1000  # Number of spins per episode

    # Experiment 1: Figure 1 10 Episodes
    num_episodes = 10
    winnings = np.zeros((num_episodes, num_spins + 1))

    for episode in range(num_episodes):
        bet_amount = 1
        episode_winnings = 0

        for spin in range(1, num_spins + 1):
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bet_amount = 1  # Reset bet on win
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2  # Double bet on loss

            winnings[episode, spin] = episode_winnings

            # Stop betting if $80 winnings are reached
            if episode_winnings >= 80:
                winnings[episode, spin:] = episode_winnings
                break

    # Plot results for 10 episodes
    plt.figure(figsize=(10, 6))
    for episode in range(num_episodes):
        plt.plot(winnings[episode], label=f'Episode {episode + 1}')
    plt.title('Figure 1: 10 Episodes of Martingale Strategy')
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.ylim(-256, 100)
    plt.xlim(0, 300)
    plt.legend(loc='upper left', fontsize=8)
    plt.grid(True)
    plt.savefig("images/figure1_10_episodes.png")
    plt.close()

    # Figure 2: 1000 Episodes
    num_episodes = 1000
    winnings = np.zeros((num_episodes, num_spins + 1))

    for episode in range(num_episodes):
        bet_amount = 1
        episode_winnings = 0

        for spin in range(1, num_spins + 1):
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bet_amount = 1  # Reset bet on win
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2  # Double bet on loss

            winnings[episode, spin] = episode_winnings

            # Stop betting if $80 winnings are reached
            if episode_winnings >= 80:
                winnings[episode, spin:] = episode_winnings
                break

    # Calculate mean and standard deviation
    mean_winnings = np.mean(winnings, axis=0)
    std_winnings = np.std(winnings, axis=0)

    # Figure 2 - Plot mean and standard deviation
    plt.figure(figsize=(10, 6))
    plt.plot(mean_winnings, label='Mean Winnings')
    plt.plot(mean_winnings + std_winnings, label='Mean + Std Dev', linestyle='--')
    plt.plot(mean_winnings - std_winnings, label='Mean - Std Dev', linestyle='--')
    plt.title('Figure 2: Mean and Std Dev of Winnings (1000 Episodes)')
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.ylim(-256, 100)
    plt.xlim(0, 300)
    plt.legend(loc='upper left', fontsize=8)
    plt.grid(True)
    plt.savefig("images/figure2_mean_stdev.png")
    plt.close()

    # Figure 3- Calculate median winnings for each spin
    median_winnings = np.median(winnings, axis=0)

    # Figure 3- Plot median and standard deviation
    plt.figure(figsize=(10, 6))
    plt.plot(median_winnings, label='Median Winnings')
    plt.plot(median_winnings + std_winnings, label='Median + Std Dev', linestyle='--')
    plt.plot(median_winnings - std_winnings, label='Median - Std Dev', linestyle='--')
    plt.title('Figure 3: Median and Std Dev of Winnings (1000 Episodes)')
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.ylim(-256, 100)
    plt.xlim(0, 300)
    plt.legend(loc='upper left', fontsize=8)
    plt.grid(True)
    plt.savefig("images/figure3_median_stdev.png")
    plt.close()

    print("Experiment 1 completed. Plots saved in the 'images' directory.")

    # Experiment 2: 1000 Episodes with Realistic Bankroll
    bankroll_limit = 256  # Realistic bankroll limit
    num_episodes = 1000
    winnings = np.zeros((num_episodes, num_spins + 1))

    for episode in range(num_episodes):
        bet_amount = 1
        episode_winnings = 0

        for spin in range(1, num_spins + 1):
            if bet_amount > bankroll_limit + episode_winnings:
                # If bet amount exceeds available funds, bet only what is left
                bet_amount = bankroll_limit + episode_winnings

            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bet_amount = 1  # Reset bet on win
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2  # Double bet on loss

            winnings[episode, spin] = episode_winnings

            # Stop betting if $80 winnings are reached or bankroll is exhausted
            if episode_winnings >= 80 or episode_winnings <= -bankroll_limit:
                winnings[episode, spin:] = episode_winnings
                break

    # Calculate mean and standard deviation
    mean_winnings = np.mean(winnings, axis=0)
    std_winnings = np.std(winnings, axis=0)

    # Figure 4: Mean and Std Dev
    plt.figure(figsize=(10, 6))
    plt.plot(mean_winnings, label='Mean Winnings')
    plt.plot(mean_winnings + std_winnings, label='Mean + Std Dev', linestyle='--')
    plt.plot(mean_winnings - std_winnings, label='Mean - Std Dev', linestyle='--')
    plt.title('Figure 4: Mean and Std Dev of Winnings (1000 Episodes, Realistic Bankroll)')
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.ylim(-256, 100)
    plt.xlim(0, 300)
    plt.legend(loc='upper left', fontsize=8)
    plt.grid(True)
    plt.savefig("images/figure4_mean_stdev_realistic.png")
    plt.close()

    # Calculate median winnings for each spin
    median_winnings = np.median(winnings, axis=0)

    # Figure 5: Median and Std Dev
    plt.figure(figsize=(10, 6))
    plt.plot(median_winnings, label='Median Winnings')
    plt.plot(median_winnings + std_winnings, label='Median + Std Dev', linestyle='--')
    plt.plot(median_winnings - std_winnings, label='Median - Std Dev', linestyle='--')
    plt.title('Figure 5: Median and Std Dev of Winnings (1000 Episodes, Realistic Bankroll)')
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.ylim(-256, 100)
    plt.xlim(0, 300)
    plt.legend(loc='upper left', fontsize=8)
    plt.grid(True)
    plt.savefig("images/figure5_median_stdev_realistic.png")
    plt.close()

    print("Experiment 2 completed. Figures 4 and 5 saved in the 'images' directory.")


if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
    test_code()  		  	   		 	 	 			  		 			     			  	 
