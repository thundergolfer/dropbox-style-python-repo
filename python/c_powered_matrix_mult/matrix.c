#include <stdio.h>
#include <stdlib.h> 
#include <time.h>
#include "matrix.h"

typedef struct {
    int *elements;
    int rows;
    int columns;
} matrix;

void _deallocate(matrix *c) {
   free(c->elements);

   c->elements = NULL;
   c->rows = 0;
   c->columns = 0;
}

void _display(matrix *z) {
   int x = 0;

   for (int i = 0; i < z->rows; i++) {
      printf("[  ");
      for (int j = 0; j < z->columns; j++) {
         printf("%-4d", z->elements[x++]);
      }
      printf("]\n");
   }
}

//this will generate random number in range [l, r]
int _generate_random(int l, int r) {
   return (rand() % (r - l + 1)) + l;
}

void multiply(matrix *a, matrix *b, matrix *c) {
   if (a->columns !=  b->rows) {
      fprintf(stderr, "The inner dimensions of your matrices do not match! Multiplication cannot be done!\n");
      // TODO(Jonathon): This unfortunately just crashes the calling Python process.
      exit(1);
   }

   c->elements = calloc(a->rows * b->columns, sizeof(int));
   c->columns = b->columns;
   c->rows = a->rows;

   int alc = 0;
   for (int x = 0; x < a->rows; x++) {
      for (int y = 0; y < b->columns; y++) {
         int value = 0;
         for (int z = 0; z < b->rows; z++) {
            value += a->elements[z + x * a->columns] * b->elements[y + z * b->columns];
         }

         c->elements[alc++] = value;
      }
    }
}

// function to get matrix elements entered by the user
void _get_matrix_elements(matrix *z, int row, int column) {
   z->elements = calloc(row * column, sizeof(int));
   z->rows = row;
   z->columns = column;

   int x = 0;
   int j = 0;


   for (int i = 0; i < row; i++) {
      x++;
      for (int y = 0; y < column; y++) {
         z->elements[j++] = _generate_random(0, 10); // TODO(Jonathon): Don't hardcode max matrix item val
      }
   }
}

// function to multiply two randomly initialized matrices
void multiply_random_matrices(
    int r1, 
    int c1, 
    int r2, 
    int c2
) {
    matrix first, second, result;
    // get elements of the first matrix
    _get_matrix_elements(&first, r1, c1);

    // get elements of the second matrix
    _get_matrix_elements(&second, r2, c2);

    // Multiplying first and second matrices and storing it in result
    multiply(&first, &second, &result);

   printf("The answer of Matrix (first * second) is \n\n");
   _display(&first);
   printf("\n  *\n\n");
   _display(&second);
   printf("\n  =\n\n");

    _display(&result);

   _deallocate(&first);
   _deallocate(&second);
   _deallocate(&result);
}