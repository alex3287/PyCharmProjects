#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int pythagorNumber(string &date)
{
	int s = 0, p;
	for(int i=0; i<date.length(); ++i)
	{
		if( (date[i]>='0')&&(date[i]<='9') )
			s += date[i] - '0';
	}
	while(p = s/10)
		s = p+s%10;
	return s;
}

int main()
{
	string
		date,
		flag,
		fatherName, motherName,
		name, nameFlag;
	
	int 
		pythNum,
		namesCount;

	set<char> liters;
	vector<string> goodNames;
	
	ifstream in("input.txt");
	in >> date >> flag;
	pythNum = pythagorNumber(date);

	in >> fatherName >> motherName;
	transform(fatherName.begin(), fatherName.end(), fatherName.begin(), toupper);
	transform(motherName.begin(), motherName.end(), motherName.begin(), toupper);

	for(int i=0; i<fatherName.length(); ++i)
		liters.insert(fatherName[i]);
	for(int i=0; i<motherName.length(); ++i)
		liters.insert(motherName[i]);
	
	in >> namesCount;
	for(int i=0; i<namesCount; ++i)
	{
		in >> name >> nameFlag;
		char t = toupper(name[0]);
		if (
			( name.length() == pythNum ) &&
			( liters.find(t) != liters.end() ) &&
			(flag == nameFlag)
			)
			goodNames.push_back(name);
	}
	in.close();
	std::sort(goodNames.begin(), goodNames.end());

	ofstream out("output.txt");
	if( goodNames.empty() )
		out << "Bad day" << '\n';
	else
		out << goodNames[0] << '\n';
	out.close();
	return 0;
}