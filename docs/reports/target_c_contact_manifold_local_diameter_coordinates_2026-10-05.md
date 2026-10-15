<!-- theorem-state: {"artifact_id":"ART-DAB2B4D3C8E3","canonical":true,"claim_ids":["C-CONTACT-DIAMETER-COORDINATES"],"claim_statuses":{"C-CONTACT-DIAMETER-COORDINATES":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: local diameter coordinate normal form

Date: 2026-10-05
Base main: 2f10893070387fb2fddc713202931b6c2dbabd4f
State: 2026-10-05.audit.52
Status: canonical in `2026-10-05.audit.56` as `C-CONTACT-DIAMETER-COORDINATES`; C-II and Level I remain open.

Let M be the exact unit-contact realization manifold of the nonisolated core,
modulo Euclidean motions. Audit.52 gives

    dim M = m = q-k-1.

For each active diameter edge h=ij define

    ell_h(p')=(|p'_i-p'_j|^2-D^2)/2

and let g_h be its differential on T_p M. The map G with rows g_h has
rank m: a vector in ker G kills all contact rows and all active diameter
rows, so canonical mixed rigidity makes it Euclidean, hence zero in the
quotient.

For the positive normalized KKT coefficients beta_h,

    sum_H beta_h g_h=0,   beta_h>0,   sum_H beta_h=1.

Thus zero lies in the interior of conv{g_h}. Therefore every nonzero
contact tangent has active diameter derivatives of both signs. By Taylor
expansion on the smooth manifold, there is a point-dependent r>0 such that
every noncongruent p' in M with 0<dist(p',p)<r has some old active diameter
strictly larger than D. This is a finite local result; no uniform r is
claimed.

Choose B subset H with |B|=m and rows g_b a basis. Put R=H minus B. Using
d_H=q-h and k=d_H+s_Z,

    |R|=h-m=s_Z+1.                                      (1)

The map p' -> (ell_b(p'))_{b in B} has invertible derivative. Hence the
inverse function theorem makes y=(ell_b) exact local coordinates on M.
Write the other active excesses as rho(y). If A=D rho(0), KKT stationarity
becomes

    beta_B + A^T beta_R=0.                              (2)

Hence every nonzero componentwise y<=0 satisfies

    beta_R^T A y=-beta_B^T y>0,                         (3)

so some residual active diameter has positive first variation.

The exact audit.52 energy identity gives the finite formula

    beta_R^T rho(y)
      = -beta_B^T y - E_Omega(y)/2,                     (4)

where E_Omega(y)>=0 and smoothness gives E_Omega(y)=O(||y||^2). Therefore,
for all sufficiently small nonzero y<=0, beta_R^T rho(y)>0 and some
residual diameter is strictly longer than D.

Finally dim ker(G^T)=h-m=s_Z+1. Since G_B is invertible, restriction
lambda -> lambda_R is an isomorphism ker(G^T) -> R^R. The same s_Z+1
residual edges therefore parameterize every linear dependence among the
active-diameter covectors.

This narrows active-diameter feasibility to a nonlocal problem. If
s_Z=o(D), only o(D) residual active edges remain outside a complete local
diameter-coordinate basis, while audit.52 forces a linear
direction-frustrated chamber bank. If s_Z=Omega(D), s_Z itself is linear
mixed-rigidity currency. No computation or verifier is used.

## Preservation status and provenance (2026-10-05)

Recovered from `automation/target-c-contact-manifold-diameter-cage-2026-10-05-v2`
at source tip `ed96cf2a2158f27c31c986a7626fccbf21522fdd`. The source is based
on main `2f10893070387fb2fddc713202931b6c2dbabd4f` at `audit.52`; main has
since advanced to `audit.54`. The local-coordinate and residual-diameter claims were independently re-audited against the audit.55 stack and promoted in `2026-10-05.audit.56`. No standalone verifier is needed for the finite linear-algebra/implicit-function argument. The theorem does not establish a global diameter improvement or close C-II.
