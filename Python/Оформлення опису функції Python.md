```python

from typing import List, Optional


def calculate_weighted_average(
    values: List[float], weights: Optional[List[float]] = None
) -> float:
  """Обчислює зважене середнє арифметичне для заданого списку значень.

  Детальніший опис логіки функції, якщо це необхідно. Тут можна вказати
  особливості обробки крайових випадків або алгоритму.

  Args:
      values (List[float]): Список числових значень для обчислення.
      weights (Optional[List[float]], optional): Список ваг для кожного значення.
        За замовчуванням None (усі ваги вважаються рівними 1).

  Returns:
      float: Обчислене зважене середнє значення.

  Raises:
      ValueError: Якщо список values порожній або довжини values та weights не
      збігаються.

  Example:
      >>> calculate_weighted_average([4.0, 5.0], [1.0, 2.0])
      4.666666666666667
  """
  if not values:
    raise ValueError("Список значень не може бути порожнім.")

  if weights is not None and len(values) != len(weights):
    raise ValueError("Довжина списку значень і списку ваг повинна збігатися.")

  if weights is None:
    return sum(values) / len(values)

  total_weight = sum(weights)
  if total_weight == 0:
    raise ValueError("Сума ваг не може дорівнювати нулю.")

  weighted_sum = sum(v * w for v, w in zip(values, weights))
  return weighted_sum / total_weight
