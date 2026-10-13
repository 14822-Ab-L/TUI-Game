# [Game Name TBD] — Game Design Document

Status: Revised draft for review
Last updated: 13 October 2026

This document records the current design. Exact balance values, implementation details, and team assignments remain open unless specified.

## 1. Game concept

A text-based stock-trading game with roguelike elements and a casino theme. The player starts with a lump sum of cash and a fixed debt, then has 10 turns to build enough wealth to cover that debt and earn a high score.

The main challenge is interpreting news and connecting it to fictional companies. Headlines and company names are silly and meme-inspired, but their economic connections should make sense if the player pays attention. The game pokes fun at day traders without relying on real political controversies.

Between trading turns, the player gets one free play of a chosen casino minigame. Random news selection and minigame outcomes create variety between runs.

## 2. Player objective and run length

- A run lasts exactly 10 playable turns.
- Whether turns are presented as days or weeks is TBD.
- Survive the run and cover the fixed debt at final settlement.
- Three consecutive turns ending with a negative cash balance cause an early loss.
- A limited overdraft allows the cash balance to go slightly negative. Its limit is TBD.
- Debt is settled automatically at the end; there are no manual or daily repayments.
- After final settlement, any surplus is the player's high score.
- If final assets cannot cover the debt, the player loses.
- Whether an exact zero surplus counts as a win is TBD.

Final score = cash balance + final value of stock holdings − fixed debt

Example: $182,000 in final assets minus $100,000 debt gives a score of $82,000. These are illustrative amounts, not confirmed starting values.

## 3. Core gameplay loop

1. At the start of a turn, apply the previous turn's news effects to stock prices. Turn 1 uses starting prices.
2. Present six new headlines: three impactful stories and three filler stories, mixed together.
3. The player interprets the news and buys, sells, or holds stocks. These headlines predict the next market update.
4. The player ends trading and chooses one minigame for a free play.
5. Add any minigame winnings to cash, then check the negative-balance streak.
6. Advance to the next turn if the run continues.

After turn 10, resolve its news effects as a final market update, automatically sell all holdings, and deduct the fixed debt. This is settlement, not an eleventh playable turn.

The central decision is identifying which news matters, what it means for a company, and how much money to commit. The minigame choice depends on whether the player wants a modest lifeline, a reward influenced by skill, or a chance at a jackpot.

The exact ordering of the final negative-balance check and settlement remains an implementation decision to confirm.

## 4. Main mechanics

### Stocks and trading

- The current screen design contains five stocks.
- Company names should immediately communicate their industry.
- Example names: Bombs R Us and Big Medical Company.
- Players can buy shares, sell owned shares, or hold them.
- Prices change through predetermined effects attached to news stories.
- Track shares owned and the average purchase price of the currently held shares.
- Buying the same stock at different prices updates its average purchase price.
- Example: 10 shares at $100 plus 10 at $120 gives an average purchase price of $110.
- Quantity controls, starting prices, rounding, and trading limits are TBD.

### Casino minigames

The minigame phase is mandatory. The player chooses one game and gets exactly one free play per turn. It never deducts from their cash balance; an unsuccessful play awards $0.

| Minigame | Intended role |
| --- | --- |
| Slots | Usually little or no reward, with the highest payout ceiling through a rare jackpot. Appeals to players who can afford a miss or need a large rescue. |
| Blackjack | Player decisions and skill influence the outcome. |
| Heads or tails | A true 50/50 chance at a fixed reward; intended as the safest, simplest lifeline. No guaranteed bonus. |

All three are intended for the initial game, subject to available development time. Exact payouts, slot probabilities, and blackjack rules are TBD. Additional minigames may follow.

### Money and resources

- Cash balance: spendable money, including any permitted overdraft.
- Holdings value: shares valued at current stock prices.
- Fixed debt: the separate amount deducted at final settlement.
- Net worth: cash plus holdings value minus fixed debt.
- Buying stock reduces cash and increases holdings; it does not immediately reduce net worth.
- Starting cash, fixed debt, and overdraft limit are TBD.

## 5. Run variety and progression

Confirmed sources of variety are random news selection and minigame outcomes.

Each run has its own news selection, trading decisions, and financial outcome. Permanent progression, unlocks, upgrades, difficulty modifiers, and carryover between runs have not been defined. The current focus is making the 10-turn loop enjoyable.

## 6. News system

### Impactful stories

- Handcraft a target pool of approximately 80 impactful stories.
- Each story has a headline, an affected stock, and a predetermined percentage change.
- Randomness selects the story; its effect is authored rather than randomly generated.
- Some connections can be obvious and others less direct, but they should remain logical.
- Example: “Penguins announce invasion of New Zealand” increases Bombs R Us by 30% at the next market update.
- Whether multiple stories may affect the same stock in one turn, and how those effects combine, is TBD.

### Filler stories

- Filler has no stock effect.
- Use believable everyday reporting to give the ticker the feel of a real news broadcast.
- Example: “Cat stuck in tree; local man rescues.”
- Filler should avoid accidentally implying a meaningful effect on an available stock.

### Selection

- Draw three impactful and three filler stories per turn.
- Select randomly without repeating a story within the same run.
- Mix the six stories for display so their placement does not identify their category.
- Ten turns require at least 30 distinct impactful and 30 distinct filler stories.
- Repeating the day's headlines as the ticker loops is expected; selecting those stories again on a later turn is not.

## 7. Interface and controls

The main trading screen is the majority of the player experience. Establish its layout early, then focus development on reliable systems, bug fixes, and enjoyable minigames.

### Top information strip

Player name, turn counter, cash balance, net worth, and debt.

A visible negative-balance streak indicator is proposed to make the early-loss rule clear.

### Main stock table

| Stock | Buy / Sell | Stocks owned | Average buy price | Current price | Change last turn |
| --- | --- | --- | --- | --- | --- |
| Bombs R Us | + / − | 10 | $100 | $130 | +30% |

See UI_Draft_V1.png for a visual example.

Current price and percentage change occupy separate, clearly aligned columns. Values above are illustrative.

### Scrolling news ticker

- Place a TV-style news ticker below the stock table.
- Scroll the current turn's headlines horizontally, separated visibly.
- Keep trading controls responsive while the ticker moves.
- A stationary “View news” list is proposed for rereading clues; its control is TBD.

### Bottom area

End turn, other menu controls, and an ASCII meme logo. Settings, exit, and save appeared in the sketch; their exact behaviour and initial scope remain TBD.

The minigame selection, individual minigame screens, and final results screen still need layouts. Exact keyboard controls and terminal size requirements are TBD.

## 8. Development milestones

### First integration milestone — proposed

Complete one playable turn: display news, trade, end the turn, play one working minigame, and return to updated prices and balances. Use this to verify that the systems connect correctly.

### Initial complete game

- Main trading screen with five stocks and the agreed columns.
- Responsive scrolling news ticker.
- Random news selection without repeats within a run.
- Buying, selling, holdings, and average purchase price tracking.
- Ten-turn run and final news resolution.
- Fixed debt settlement and final score calculation.
- Limited overdraft and three-turn negative-balance loss rule.
- Blackjack, slots, and heads or tails with one free play per turn.
- Clear win, loss, and results screens.

The first complete version is playable from starting a run through an early loss or final settlement. It should receive bug fixing and gameplay testing before expanding its scope.

## 9. Development and team responsibilities

Planned technology: Python with curses.

## 10. Future ideas

- Additional minigames, depending on time.
- Expanded news content.
- Further features only after the core loop is reliable and enjoyable.
- Whatever else the team wants

## 11. Open questions

- Final game name and five company names.
- Days or weeks as the presentation of turns.
- Starting cash, debt, stock prices, and overdraft limit.
- Multiple news effects on one stock and how they combine.
- Price floors, zero-price stocks, and rounding.
- Exact order of final loss checks and settlement.
- Whether zero surplus counts as a win.
- Minigame rules, probabilities, and payouts.
- Keyboard controls, buying quantities, and minimum terminal size.
- Save/load and high-score storage or submission.
- Any permanent progression or other roguelike mechanics beyond current run variety.
- Team assignments and development deadline.
