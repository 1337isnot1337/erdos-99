# Target C explicit global route-surplus floor

Date: 2026-09-12

Lifecycle: audited-working proof-only consequence; theorem-state authority unchanged.
C-II and Level I remain open.

Let `lambda_D=(b-per(F))/D` and let `P_exc^G=Q+4f` be the global bounded
nonquadrilateral-face endpoint capacity. The audited all-detour atomic endpoint
theorem, specialized to Fejer order two, gives

```
liminf P_exc^G/D >= (4 sqrt(Delta_2)-sqrt(U_2(lambda)))_+,
U_2(lambda)=((pi+lambda)^2+1225 lambda^2)/2.
```

Since `U_2` is increasing, at `lambda=1/10` the elementary bounds
`sqrt(Delta_2)>9/10` and `sqrt(U_2(1/10))<7/2` give a strict lower margin above
`1/10`. Splitting into `lambda<=1/10` and `lambda>=1/10` yields the global floor

```
liminf [(b-per(F))+P_exc^G]/D >= 1/10.             (GR.1)
```

This is genuinely global: it does not identify `P_exc^G` with the sum of local
harmonic-cell endpoint capacities. Canonical Section 123 only pays the local quantity
by `10(e_BB-k)`, so (GR.1) is not yet a C-II contradiction. The unresolved bridge is
to couple the global route currency to the local aggregate detour without silently
assuming local/global face injectivity, or to turn the forced global route surplus
into a source-preserving strict diameter decrease.
