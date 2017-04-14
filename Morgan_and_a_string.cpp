#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdint>
#include <math.h>
#include <stdlib.h>


using namespace std;





int main()
{
	//get number of test cases
	string n2 ;
	getline(cin , n2);
	int n =atoi(n2.c_str());
	
	//store all test cases in vector
	vector < string > all_lines(2*n);
	
	int num_lines = 0;
	
	//read in input lines
	while (num_lines < (2 * n))
	{
		string line_current; 
		getline(cin, line_current);
		all_lines[num_lines] = line_current;
		num_lines = num_lines +1;
	}
	
	//convert input to integers
	int i = 0;
	while (i < 2 * n)
	{
		string a = all_lines[i];
		string b = all_lines[i+1];
		
		//cout << "current " << i <<" "<< a << endl;
		//cout << "current 2 " << i+1 <<" "<< b << endl;
		
		int total_size = a.length() + b.length();
		//cout << total_size << endl;
		
		int k = 0;
		int a_index = 0;
		int b_index = 0;
		
		string combined;
		while (a_index < a.length() && b_index < b.length())
		{	
			//cout << "A: " << a[a_index] << endl;
			//cout << "B: " << b[b_index] << endl;
			
			
			if (a[a_index]  > b[b_index])
			{
				combined = combined +  b[b_index];
				//cout << "Combined B: " << combined << endl;
				
				b_index = b_index + 1;
				k=k+1;
				
			}
			else if (a[a_index] < b[b_index])
			{
				combined = combined + a[a_index];
				
				a_index = a_index + 1;
				//cout << "Combined A: " << combined << endl;
				k=k+1;
			
			}
			else if (a[a_index] == b[b_index])
			{
				int temp_a = a_index;
				int temp_b = b_index;
				while (temp_a < a.length() || temp_b < b.length())
				{
					
					if (a[temp_a] == b[temp_b] && temp_a < a.length()-1 && temp_b < b.length()-1)
					{
						//cout <<"both" << endl;
						temp_a = temp_a+1;
						temp_b = temp_b+1;
					}
					//if one of the matching letters is at the end of the string
					else if (a[temp_a] == b[temp_b] && temp_a < a.length()-1 && temp_b >= b.length()-1)
					{
						//cout <<"A" << endl;
						temp_a = temp_a+1;
					}
					
					else if (a[temp_a] == b[temp_b] && temp_b < b.length()-1 && temp_a >= a.length()-1)
					{
						//cout <<"B" << endl;
						temp_b = temp_b+1;
					}
					
					else if (a[temp_a] == b[temp_b] && temp_b >= b.length()-1 && temp_a >= a.length()-1)
					{
						combined = combined + a[a_index];
						
						k = k+1;
						a_index++;
						break;
					}
					
					
					if (a[temp_a] < b[temp_b])
					{
						combined = combined + a[a_index];
						k = k+1;
						a_index++;
						break;
					
					}
					if (a[temp_a] > b[temp_b])
					{
						combined = combined + b[b_index];
						
						k = k+1;
						b_index++;
						break;
					}
				
				}
				
			
			}
		
		
		//cout << "Combined " << combined << endl;
			
		
			
		}
		
		//cout << combined.length() << endl;
			//now only one string remains, so append the remaining to the end
		if (combined.length() < total_size )
		{
			//cout <<"something left" << endl;
			if (a_index < a.length())
			{
				combined = combined + a.substr(a_index, a.length()-a_index);
			}
			if (b_index < b.length())
			{
				combined = combined + b.substr(b_index, b.length()-b_index);
			}
		
		}
		
		
		cout << combined << endl;


		
	
		i = i+2;
	}
	

	


	//cout << "woohoo" << endl;

	return 0;
}