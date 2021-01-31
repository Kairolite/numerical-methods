class TrussExampleAlt
// DECLARATIONS
// Data for each member: [element #, node i, node j, theta, area, modulus, length]
// SI Units: [integer, integer, integer, degrees, meters^2, pascals, meters]
// Imperial Units: [integer, integer, integer, degrees, inches^2, lb/inches, inches]
parameter Real [:,7] member = [1, 1, 2,      0, 10e-4, 200e9, 1;
                               2, 2, 3,      0, 10e-4, 200e9, 1;
                               3, 1, 4, 308.66, 10e-4, 200e9, 1.60;
                               4, 2, 4, 270.00, 10e-4, 200e9, 1.25;
                               5, 3, 4, 231.34, 10e-4, 200e9, 1.60];

// External loads and boundary conditions for each node: [node #, FX, FY, UX(1:Fixed), UY(1:Fixed)]
parameter Real [:,5] node_load = [1,        0,        0, 1, 1;
                                  2, -1035.28, -3863.70, 0, 0;
                                  3,        0,        0, 1, 1;
                                  4, -1035.28, -3863.70, 0, 0];

// Vector for equivalent stiffness constant of each member
Real k [size(member,1)];

// Arrays for Stiffness Matrices
Real Ke [size(member,1), 4, 4]; // Element
Real KGe [size(member,1), 2*size(node_load,1), 2*size(node_load,1)]; // Element in Global Form
Real KGt [2*size(node_load,1), 2*size(node_load,1)]; // Total Global

// Displacement Matrix
Real U [2*size(node_load,1)]; 

// Postprocessing Phase
Real R [2*size(node_load,1)]; // Reaction forces for each node
Real InForce_NormStress [size(member,1),7]; // Internal forces and normal stress for each member
// Format: [member #, uix, uiy, ujx, ujy, internal force, normal stress]

// EQUATIONS
equation

// Calculate stiffness constants for each member element
k = {(member[i,5] * member[i,6] / member[i,7]) for i in 1:size(member,1)};

// Find stiffness matrix for each element
Ke = StiffnessMatrixElement(member);

// Assemble the global stiffness matrix
KGe = StiffnessMatrixGlobal(member, node_load);
KGt = StiffnessMatrixFinal(KGe);

// Solve for the displacement matrix
U = DisplacementMatrix(node_load, KGt);

// Postprocessing Phase
(R, InForce_NormStress) = TrussPostProcess(member, node_load, KGt, U);

end TrussExampleAlt;
