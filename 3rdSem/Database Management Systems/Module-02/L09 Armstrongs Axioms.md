# Armstrongs Axioms

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 9  
**Date:** 18-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Armstrong's Axioms -- Complete Set of Inference Rules

Armstrong's axioms are a **sound and complete** set of inference rules for functional dependencies. 
- **Sound:** Every FD derived using these rules is logically implied by the original set.
- **Complete:** Every FD that is logically implied can be derived using these rules.

---

## The Three Primary Axioms

### 1. Reflexivity (Trivial Dependency Rule)

**Statement:** If `Y subset of X`, then `X -> Y`.

**Explanation:** A set of attributes always determines itself or any subset of itself. These are called **trivial dependencies**.

**Example:** Given `X = {A, B, C}`:
- `ABC -> A` (since A subset of ABC)
- `ABC -> B` (since B subset of ABC)
- `ABC -> AB` (since AB subset of ABC)
- `ABC -> ABC` (every set determines itself)

**Proof:** If two tuples have the same values for all attributes in X, they trivially have the same values for any subset Y of X. So `X -> Y` always holds.

### 2. Augmentation (Augmentation Rule)

**Statement:** If `X -> Y`, then `XZ -> YZ` for any set of attributes Z.

**Explanation:** Adding the same attributes to both the left and right sides preserves the dependency.

**Example:** Given `EmpID -> Name`:
- By augmentation with Dept: `EmpID, Dept -> Name, Dept`
- This means: if we know EmpID and Dept, we know Name and Dept.

**Proof:** Assume `t1[XZ] = t2[XZ]`. Then `t1[X] = t2[X]` (by equality on X subset of XZ). Since `X -> Y`, we have `t1[Y] = t2[Y]`. Also `t1[Z] = t2[Z]` (by equality on Z). Thus `t1[YZ] = t2[YZ]`. So `XZ -> YZ`.

### 3. Transitivity

**Statement:** If `X -> Y` and `Y -> Z`, then `X -> Z`.

**Explanation:** Functional dependencies chain together.

**Example:** 
- `EmpID -> DeptID` (each employee has one department)
- `DeptID -> Budget` (each department has one budget)
- By transitivity: `EmpID -> Budget`

**Proof:** Assume `t1[X] = t2[X]`. Since `X -> Y`, we have `t1[Y] = t2[Y]`. Since `Y -> Z`, we have `t1[Z] = t2[Z]`. Thus `X -> Z`.

---

## Additional Derived Rules

These rules are **not independent**; they can be proved using the three primary axioms.

### 4. Union Rule

**Statement:** If `X -> Y` and `X -> Z`, then `X -> YZ`.

**Proof Using Armstrong's Axioms:**
1. `X -> Y` (given)
2. `X -> Z` (given)
3. `X -> XY` (augment 1 with X: add X to both sides)
4. `XY -> YZ` (augment 2 with Y: X -> Z becomes XY -> YZ)
5. `X -> YZ` (transitivity on 3 and 4)

**Example:** If `EmpID -> DeptID` and `EmpID -> Salary`, then `EmpID -> DeptID, Salary`.

### 5. Decomposition Rule

**Statement:** If `X -> YZ`, then `X -> Y` and `X -> Z`.

**Proof:**
1. `X -> YZ` (given)
2. `YZ -> Y` (reflexivity, since Y subset of YZ)
3. `X -> Y` (transitivity on 1 and 2)

**Example:** If `EmpID -> DeptID, Salary`, then `EmpID -> DeptID` and `EmpID -> Salary`.

### 6. Pseudotransitivity Rule

**Statement:** If `X -> Y` and `WY -> Z`, then `WX -> Z`.

**Proof:**
1. `X -> Y` (given)
2. `WX -> WY` (augment 1 with W)
3. `WY -> Z` (given)
4. `WX -> Z` (transitivity on 2 and 3)

**Example:** If `DeptID -> ManagerID` and `ManagerID, Year -> Bonus`, then `DeptID, Year -> Bonus`.

---

## Proving the Derived Rules

### Prove Union Rule from Armstrong's Axioms (Detailed)

Given: `X -> Y` and `X -> Z`. Show: `X -> YZ`.

| Step | FD | Rule Used |
|------|----|-----------|
| 1 | `X -> Y` | Given |
| 2 | `X -> Z` | Given |
| 3 | `X -> XY` | Augmentation (1 with X) |
| 4 | `XY -> YZ` | Augmentation (2 with Y) |
| 5 | `X -> YZ` | Transitivity (3, 4) |

### Prove Decomposition Rule (Detailed)

Given: `X -> YZ`. Show: `X -> Y` and `X -> Z`.

| Step | FD | Rule Used |
|------|----|-----------|
| 1 | `X -> YZ` | Given |
| 2 | `YZ -> Y` | Reflexivity (since Y subset of YZ) |
| 3 | `X -> Y` | Transitivity (1, 2) |
| 4 | `YZ -> Z` | Reflexivity (since Z subset of YZ) |
| 5 | `X -> Z` | Transitivity (1, 4) |

---

## Worked Examples

### Example 1: Implication of FDs

Given `F = {A -> B, B -> C, AB -> D}`, prove that `A -> D` holds.

**Proof:**
1. `A -> B` (given)
2. `B -> C` (given)
3. `A -> C` (transitivity: 1, 2)
4. `A -> AB` (augmentation: 1 with A gives A -> AB? Actually A -> B, augment with A gives AA -> AB, i.e., A -> AB)
   Wait more carefully: `A -> B`. Augment with A: `A, A -> A, B` which is `A -> AB`.
5. `AB -> D` (given)
6. `A -> D` (transitivity: 4, 5)

### Example 2: Using All Rules

Given `R(A, B, C, D, E)` and `F = {A -> BC, CD -> E, B -> D, E -> A}`.

**Prove `A -> E`:**

1. `A -> BC` (given)
2. `A -> B` (decomposition on 1)
3. `A -> C` (decomposition on 1)
4. `B -> D` (given)
5. `A -> D` (transitivity: 2, 4)
6. `A -> CD` (union: 3, 5)
7. `CD -> E` (given)
8. `A -> E` (transitivity: 6, 7)

### Example 3: Pseudotransitivity

Given `X -> Y` and `WY -> Z`, show `WX -> Z`.

Let's use concrete attributes: `EmpID -> DeptID` and `DeptID, Location -> Budget`. Show: `EmpID, Location -> Budget`.

1. `EmpID -> DeptID` (given)
2. `EmpID, Location -> DeptID, Location` (augmentation of 1 with Location)
3. `DeptID, Location -> Budget` (given)
4. `EmpID, Location -> Budget` (transitivity: 2, 3)

---

## Soundness and Completeness

**Soundness:** Every FD derived using Armstrong's axioms is logically implied by the original set `F`. We proved this for each axiom.

**Completeness:** Every FD that is logically implied by `F` can be derived using Armstrong's axioms. The proof uses the concept of attribute closure. If `X -> Y` is logically implied by `F`, then `Y subset of X+`, and we can derive `X -> Y` by:
1. Deriving `X -> X+` by repeatedly applying axioms
2. Decomposing to get `X -> Y`

---

## Practice Problems

1. Given `F = {A -> B, B -> C, C -> D}`, prove `A -> D` using Armstrong's axioms. State each rule used.

2. Given `F = {AB -> C, B -> D, C -> E}`, can we derive `AB -> E`? Show the steps.

3. Using Armstrong's axioms, prove the union rule (if `X -> Y` and `X -> Z` then `X -> YZ`).

4. Given `R(A, B, C, D)` with `F = {A -> BC, CD -> B}`, prove `A -> B`.

5. What does it mean for Armstrong's axioms to be "complete"?

**Answers:**
1. 
- `A -> B` (given)
- `B -> C` (given)
- `A -> C` (transitivity: A->B, B->C)
- `C -> D` (given)
- `A -> D` (transitivity: A->C, C->D)

2. 
- `AB -> C` (given)
- `C -> E` (given)
- `AB -> E` (transitivity: AB->C, C->E)

3. See the detailed proof above.

4. 
- `A -> BC` (given)
- `A -> B` (decomposition)
Direct! No need for CD -> B.

5. Completeness means that every FD that is logically implied by a set F can be derived using Armstrong's axioms. There is no implied FD that the axioms miss.
