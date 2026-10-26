<?php
declare(strict_types=1);

/** Public synthetic example: no credentials or external services. */
function sumNonNegative(int $a, int $b): int
{
    if ($a < 0 || $b < 0) {
        throw new InvalidArgumentException('Expected non-negative operands');
    }
    if ($a > PHP_INT_MAX - $b) {
        throw new OverflowException('Integer overflow');
    }
    return $a + $b;
}
