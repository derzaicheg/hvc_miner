FOR /L %%A IN (1,1,200) DO (
  ECHO %%A
  waitfor SomethingThatIsNeverHappening /t 1
)