class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    count = collections.Counter(tasks)
    maxFreq = max(count.values())
    # Put the most frequent task in the slot first.
    maxFreqTaskOccupy = (maxFreq - 1) * (n + 1)
    # Get the number of tasks with same frequency as maxFreq, we'll append them after the
    # `maxFreqTaskOccupy`.
    nMaxFreq = sum(value == maxFreq for value in count.values())
    return max(maxFreqTaskOccupy + nMaxFreq, len(tasks))
