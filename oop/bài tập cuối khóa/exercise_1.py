# a
'''
public - ở dạng kế thừa public thì sau khi kế thừa, tất cả các thành viên dang public trong lớp cha sẽ vẫn là public trong lớp con, dạng protected ở lớp cha vẫn sẽ là protected ở lớp con

protected - nếu dùng protected thì sau khi kế thừa, tất cả các thành viên dạng public ở lớp cha sẽ trở thành protected tại lớp con

private - khi sử dụng private thì sau khi kế thừa, tất cả các thành viên dạng public và protectied ở lớp cha sẽ trở thành private tại lớp con
'''

# b
'''
các đặc điểm quan trọng của lập trình hướng đối tượng:
- tính đóng gói: các đối tượng và phương thức liên quan được đóng gói thành từng class nhỏ và được xây dụng để thực hiện một nhóm chức năng đặc trưng riêng. đặc tính này còn giúp tránh sự rò rỉ thông tin ra bên ngoài

- tính kế thừa: các lớp dữ liệu mang tính kế thừa nhau. lớp cha có thể chia sẻ các dữ liệu và phương thức cho các lớp con, từ đó các lớp con có thể kế thừa và bổ sung thêm các thành phần mới của riêng mình

- tính đa hình: sử dụng lớp con giống hệt như lớp cha, nhưng mỗi lớp con vẫn giữ nguyên method của mình.

- tính trừu tượng: các đối tượng được tạo ra từ các lớp có thể được sử dụng như nhau, mà không cần quan tâm đến cách thức hoạt động bên trong của chúng. nhìn chung, tính trừu tượng giúp cô lập sự ảnh hưởng của sự thay đổi mã code để nếu có si sót gì xảy ra, ảnh hưởng cua rsự thay đổi là không nhiều.
'''