#!/usr/bin/python3

"""
magic_calculation - Replicates the behavior of given Python bytecode
"""

def magic_calculation(a, b):
        add, sub = __import__('magic_calculation_102', globals(), locals(), ['add', 'sub']).add, __import__('magic_calculation_102', globals(), locals(), ['add', 'sub']).sub
            
                if a < b:
                            c = add(a, b)
                                    
                                            for i in range(4, 6):
                                                            c = add(c, i)
                                                                    
                                                                            return c
                                                                            else:
                                                                                        return sub(a, b)

                                                                                    if __name__ == "__main__":
                                                                                            pass  # Add test cases or additional functionality if needed

