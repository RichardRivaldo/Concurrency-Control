# Concurrency-Control

Database Management: Concurrency Control Protocol in Transactions

### Algorithm

* `Simple Locking` (`Exclusive Locks` only)

### Executing the Program

* Just run the `main.py` file from the root directory of the repository.
* You can find the operations that will be executed by the concurrency protocol at the `utils.py` file. You can change
  it accordingly to the operation that you want to check.
* Please remember that the program assumes that the `Commit Operation` will be correctly placed for each transaction,
  that is in the end of the transaction.

### Output

* The program will show the initial operations that you give to the `Simulator`.
* The `Lock Manager` will manage the locks while also executing the program and saving it to its `Schedule`.
* Execution of the program will be directly connected to the dummy `Data` struct that each has value of its own. The
  final states of the data will also be shown by the simulator.
* Lastly, the simulator will also show the final generated schedule based on the algorithm.

### Simple Locking (Exclusive Locks)

* This algorithm is a simplified version of lock-based Two-Phase Locking Protocol. The original version actually has two
  versions of locks: `Shared Lock` and `Exclusive Lock`, while this program only has the latter one.
* Shared Lock is given for `Read` operations and Exclusive Lock is given for `Write` operations.
* The algorithm itself has many variants regarding when to grant and release the locks given to a transaction. Some of
  them are `Strict Two-Phase Locking` and `Rigorous Two-Phase Locking`.
* The first one releases exclusive locks of a transaction when the transaction commits or is aborts, while the second
  one releases all the locks with the same condition.
* The implementation is similar, except that Read operation is also given Exclusive Locks by the Lock Manager. The locks
  are granted for an operation when the operation is going to be executed. This is different
  to `Conservative Two-Phase Locking` which grants the locks before the transaction is executed.
* If a transaction A is blocked by another transaction which currently holds the lock requested by the transaction A, it
  will do the following.
    * If the transaction has only one operation (excluding commits), then the transaction will be added to the waiting
      queue and will continue when the lock is released for the requested data of the pending operation.
    * Else, then the transaction will be aborted. The transaction will be rescheduled to be executed after all other
      operations in the original schedule are finished.

### References

* [Database Concurrency Protocol by David Hatch and Kun Ren](https://github.com/dhatch/database-concurrency-control)