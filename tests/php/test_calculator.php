<?php
declare(strict_types=1);
require_once __DIR__ . '/../../examples/php/Calculator.php';

function expectSame($want, $got): void {
    if ($want !== $got) {
        throw new RuntimeException('Unexpected result');
    }
}
expectSame(5, sumNonNegative(2, 3));
expectSame(0, sumNonNegative(0, 0));
try {
    sumNonNegative(-1, 1);
    throw new RuntimeException('Negative input was accepted');
} catch (InvalidArgumentException $expected) {
    // passed
}
try {
    sumNonNegative(PHP_INT_MAX, 1);
    throw new RuntimeException('Overflow was accepted');
} catch (OverflowException $expected) {
    // passed
}
echo "4 public PHP assertions passed\n";
