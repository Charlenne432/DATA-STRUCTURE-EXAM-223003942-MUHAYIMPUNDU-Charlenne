#include <iostream>
#include <cstring>
using namespace std;

// 1. Define struct Contact
struct Contact {
    char name[30];
    char phone[15];
};

// Function to dynamically allocate Contact array
Contact* allocateContacts(int count) {
    return new Contact[count];
}

// 2. Abstract class ContactBase
class ContactBase {
public:
    char name[30];
    char phone[15];

    ContactBase(const char* n, const char* p) {
        strncpy(name, n, 29); name[29] = '\0';
        strncpy(phone, p, 14); phone[14] = '\0';
    }

    virtual void display() = 0; // Pure virtual function
    virtual ~ContactBase() {}
};

// Derived class FriendContact
class FriendContact : public ContactBase {
public:
    char relation[20];

    FriendContact(const char* n, const char* p, const char* r)
        : ContactBase(n, p) {
        strncpy(relation, r, 19); relation[19] = '\0';
    }

    void display() {
        cout << "Friend: " << name << ", Phone: " << phone
             << ", Relation: " << relation << endl;
    }
};

// Derived class ColleagueContact
class ColleagueContact : public ContactBase {
public:
    char jobTitle[20];

    ColleagueContact(const char* n, const char* p, const char* jt)
        : ContactBase(n, p) {
        strncpy(jobTitle, jt, 19); jobTitle[19] = '\0';
    }

    void display() {
        cout << "Colleague: " << name << ", Phone: " << phone
             << ", Job Title: " << jobTitle << endl;
    }
};

// 3. ContactBase** allContacts
ContactBase** allContacts = NULL;
int contactCount = 0;

// 4. Define Group struct
struct Group {
    char groupName[20];
    ContactBase** members;
    int memberCount;

    Group(const char* name) {
        strncpy(groupName, name, 19); groupName[19] = '\0';
        members = NULL;
        memberCount = 0;
    }

    void addMember(ContactBase* contact) {
        ContactBase** newMembers = new ContactBase*[memberCount + 1];
        for (int i = 0; i < memberCount; ++i)
            newMembers[i] = members[i];
        newMembers[memberCount] = contact;
        ++memberCount;
        delete[] members;
        members = newMembers;
    }

    void removeMember(const char* nameToRemove) {
        int index = -1;
        for (int i = 0; i < memberCount; ++i) {
            if (strcmp(members[i]->name, nameToRemove) == 0) {
                index = i;
                break;
            }
        }
        if (index == -1) return;

        ContactBase** newMembers = new ContactBase*[memberCount - 1];
        for (int i = 0, j = 0; i < memberCount; ++i) {
            if (i != index) newMembers[j++] = members[i];
        }
        delete[] members;
        members = newMembers;
        --memberCount;
    }

    void displayGroup() {
        cout << "\nGroup: " << groupName << " (" << memberCount << " members)\n";
        for (int i = 0; i < memberCount; ++i) {
            members[i]->display(); // Polymorphic call
        }
    }

    ~Group() {
        delete[] members;
    }
};

// 5. Group management
Group** groups = NULL;
int groupCount = 0;

void addGroup(const char* name) {
    Group** newGroups = new Group*[groupCount + 1];
    for (int i = 0; i < groupCount; ++i)
        newGroups[i] = groups[i];
    newGroups[groupCount] = new Group(name);
    ++groupCount;
    delete[] groups;
    groups = newGroups;
}

void removeGroup(const char* nameToRemove) {
    int index = -1;
    for (int i = 0; i < groupCount; ++i) {
        if (strcmp(groups[i]->groupName, nameToRemove) == 0) {
            index = i;
            break;
        }
    }
    if (index == -1) return;

    delete groups[index];
    Group** newGroups = new Group*[groupCount - 1];
    for (int i = 0, j = 0; i < groupCount; ++i) {
        if (i != index) newGroups[j++] = groups[i];
    }
    delete[] groups;
    groups = newGroups;
    --groupCount;
}

// MAIN PROGRAM
int main() {
    // Allocate contacts
    Contact* rawContacts = allocateContacts(2);
    strncpy(rawContacts[0].name, "John", 29);
    strncpy(rawContacts[0].phone, "123456", 14);
    strncpy(rawContacts[1].name, "Emma", 29);
    strncpy(rawContacts[1].phone, "987654", 14);

    // Create polymorphic contacts
    allContacts = new ContactBase*[2];
    allContacts[0] = new FriendContact("John", "123456", "School");
    allContacts[1] = new ColleagueContact("Emma", "987654", "Engineer");
    contactCount = 2;

    // Display all contacts
    cout << "All Contacts:\n";
    for (int i = 0; i < contactCount; ++i) {
        allContacts[i]->display(); // Polymorphic call
    }

    // Add a group
    addGroup("WorkGroup");
    groups[0]->addMember(allContacts[0]);
    groups[0]->addMember(allContacts[1]);
    groups[0]->displayGroup();

    // Remove one member
    groups[0]->removeMember("John");
    groups[0]->displayGroup();

    // Remove the group
    removeGroup("WorkGroup");

    // Cleanup
    for (int i = 0; i < contactCount; ++i)
        delete allContacts[i];
    delete[] allContacts;
    delete[] rawContacts;
    delete[] groups;

    return 0;
}

